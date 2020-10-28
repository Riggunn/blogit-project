from django.shortcuts import render, redirect
from blogs.models import Blog
from profiles.models import Profile
from comments.models import Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from django.http import HttpResponse
from taggit.models import Tag
# Create your views here.
@login_required
def single_blog(request, blog_id):

    blog = Blog.objects.get(id=str(blog_id))
    profile = Profile.objects.get(user=request.user)
    
    latest_blogs = Blog.objects.filter(is_published=True).order_by('created_at')[:4]

    tags = Tag.objects.all()

    context = {
        'blog': blog,
        'profile': profile,
        'latest_blogs': latest_blogs,
        'tags': tags,
        }
    return render(request, 'blogs/single_blog.html', context=context)

@login_required
def leave_comment_to_blog(request, blog_id):
    if request.method == 'POST':
        blog = Blog.objects.get(id=str(blog_id))
        profile = Profile.objects.get(user=request.user)
        comment = Comment()
        comment.author = profile
        comment.text = request.POST.get('text', '---')
        comment.save()
        blog.comments.add(comment)
        blog.save()
        return redirect('single_blog', blog_id=blog_id)

@login_required
def delete_comment(request, blog_id, comment_id):
    comment = Comment.objects.get(id=str(comment_id))
    comment.delete()
    return redirect('single_blog', blog_id=blog_id)

@login_required
def add_or_remove_like(request, blog_id):
    blog = Blog.objects.get(id=str(blog_id))
    profile = Profile.objects.get(user=request.user)
# Обращение к списку лайков
    if profile.id in blog.likes:
        blog.likes.remove(profile.id)
    else:
        blog.likes.append(profile.id)
    blog.save()
    return redirect('single_blog', blog_id=blog_id)

@login_required
def add_or_remove_like_ajax(request):
    if request.is_ajax():
        blog_id = request.POST.get('blog_id')
        blog = Blog.objects.get(id=str(blog_id))
        profile = Profile.objects.get(user=request.user)
# Обращение к списку лайков
        like_color = ''
        if profile.id in blog.likes:
            blog.likes.remove(profile.id)
            like_color = 'empty'
        else:
            blog.likes.append(profile.id)
            like_color = 'red'
        blog.save()
        return HttpResponse(json.dumps(
            {
                'likes': len(blog.likes),
                'like_color': like_color
                }
                ),
                content_type='application/json'
                )

@login_required
def create_blog(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {
        'profile': profile
        }
    if request.method == 'GET':
        return render(request, 'blogs/create_blog.html', context=context)
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        tags = request.POST['tags'].replace(' ', '').lower().split(',')
        blog = Blog()
        blog.title = title
        blog.text = text
        blog.author = profile
        try:
            if any(request.FILES):
                blog.image = request.FILES['image']
        except:
            messages.error(request, 'Blog Image is not correct!')
            return render(request, 'blog/create_blog.html', context=context)
        blog.save()
        if tags:
            for tag in tags:
                blog.tags.add(tag)
        blog.save()
        messages.success(request, 'Blog successfully created!')
        return redirect('/profiles/profile/{}'.format(user.username))

@login_required
def edit_blog(request, blog_id):
    user = request.user
    profile = Profile.objects.get(user=user)
    blog = Blog.objects.get(id=str(blog_id))
    if user.id != blog.author.user.id:
        messages.error(request, "You can't edit not your blog!")
        return redirect('index')
    tags = ",".join(blog.tags.names()).strip()
    context = {
        'profile': profile,
        'blog': blog,
        'tags': tags
        }
    if request.method == 'GET':
        return render(request, 'blogs/edit_blog.html', context=context)

    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        tags = request.POST['tags'].replace(' ', '').lower().split()
# blog edit 
        blog.title = title
        blog.text = text
        if 'is_published' in request.POST:
            blog.is_published = True
        else:
            blog.is_published = False
        if tags:
            blog.tags.clear()
            for tag in tags:
                blog.tags.add(tag)
        try:
            if any(request.FILES):
                blog.image = request.FILES['image']
        except:
            messages.error(request, 'Blog Image is not correct!')
            return render(request, 'blog/create_blog.html', context=context)
        blog.save()
        messages.success(request, 'Blog successfully updated!')
        return redirect('/profiles/profile/{}'.format(user.username))

@login_required
def delete_blog(request, blog_id):
    user = request.user
    profile = Profile.objects.get(user=user)
    blog = Blog.objects.get(id=str(blog_id))
    if user.id != blog.author.user.id:
        messages.error(request, "You can't delete not your blog!")
        return redirect('index')
    context = {
        'profile': profile,
        'blog': blog
        }
    blog.delete()
    messages.success(request, 'Blog successfully deleted!')
    return redirect('/profiles/profile/{}'.format(user.username))