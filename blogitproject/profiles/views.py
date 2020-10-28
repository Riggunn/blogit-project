# views.py -- profiles
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required
def user_profile_page(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    context = {
        'profile': profile
    }
    return render(request, 'profiles/profile.html', context=context)

@login_required
def user_profile_edit_page(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    context = {'profile': profile}
    
    if request.method == 'GET':
        return render(request, 'profiles/profile_edit.html', context=context)
    
    if request.method == 'POST':
        # parse request data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        status = request.POST['status']
        about = request.POST['about']
        # update User fields
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        # update Profile fields
        profile.status = status
        profile.about = about
        try:
            if any(request.FILES):
                profile.profile_image = request.FILES['profile_image']
        except:
            messages.error(request, 'Profile Image is not correct!')
            return render(request, 'profiles/profile_edit.html', context=context)
        else:
            is_image_changed = True
        
        profile.save()
        if is_image_changed:
            profile.change_profile_image_thumbnail()
        messages.success(request, 'Profile successfully changed!')
        return redirect('/profiles/profile/{}'.format(user.username))