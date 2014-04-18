from django.shortcuts import render, get_object_or_404
from blog.models import Post
# Create your views here.

def home(request):
	return render(request, 'home.html', {'none':''})

def blog(request):
	posts = Post.objects.all()
	return render(request, 'blog.html', { 'posts': posts })

def getpost(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'getpost.html', {'post':post} )
