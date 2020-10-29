from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog
from profiles.models import Profile
from taggit.models import Tag
# Create your views here.
@login_required
def index(request):
    blogs = Blog.objects.filter(is_published=True).order_by('-created_at')
    profile = Profile.objects.get(user=request.user)
    latest_blogs = blogs[:4]

    tags = Tag.objects.all()

    if request.method == 'GET':
        search = request.GET.get('search', '')
        if search:
            blogs = blogs.filter(text=search)
        
        sort_by = request.GET.get('sort_by', '')
        if sort_by:
            sort_by_dict = {
                'a-z': 'title',
                'z-a': '-title',
                'new-old': '-created_at',
                'old-new': 'creted_at',
            }
            sort_by_param = sort_by_dict.get(sort_by)
            blogs = blogs.order_by('title')

        filter_by_tag = request.GET.get('filter_by_tag', '')
        if filter_by_tag:
            blogs = blogs.filter(tags__name__icontains=filter_by_tag)
    context = {
        'blogs': blogs,
        'profile': profile,
        'latest_blogs': latest_blogs,
        'tags': tags,
        }
    return render(request, 'pages/index.html', context=context)