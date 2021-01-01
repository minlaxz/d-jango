from django.shortcuts import render
from django.utils import timezone

from .models import Blog as Post
# from pylaxz.utils import logxs

# Create your views here.
def post_list(request):
    # logxs.printf('Got request :', _int=True)
    # logxs.printf(request)

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'postsss':posts})

