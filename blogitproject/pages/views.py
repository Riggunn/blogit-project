from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog
from profiles.models import Profile
# Create your views here.
@login_required
def index(request):
    blogs = Blog.objects.all()
    profile = Profile.objects.get(user=request.user)
    context = {
        'blogs': blogs,
        'profile': profile,
        }
    return render(request, 'pages/index.html', context=context)