from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        content = request.POST['content']
        Post.objects.create(nickname=nickname, content=content, created_at=timezone.now())
        return redirect('post_list')
    return render(request, 'post_form.html')