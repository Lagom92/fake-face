from django.shortcuts import render
from .forms import PostForm
# Create your views here.

def list(request):
    return render(request, 'posts/list.html')
    
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = PostForm()
    return render(request, 'posts/form.html', {'form':form})