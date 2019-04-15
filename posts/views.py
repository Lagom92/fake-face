from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
# Create your views here.

def list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts':posts})
    
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = PostForm()
    return render(request, 'posts/form.html', {'form':form})
    
def update(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/form.html', {'form':form})