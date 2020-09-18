from django.shortcuts import render
from django.con
trib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    context = {}
    return render(request, 'pages/index.html', context=context)