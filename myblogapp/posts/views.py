from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def index(request):
    # return HttpResponse("Hello World!")
    posts = Post.objects.order_by('-published')
    # return render(request,'posts/index.html',{'posts':posts})
    return render(request, 'posts/index.html', {'posts': posts})
    # renderはhtmlを読みだすファイル
    # posts/index.htmlはdirectoryの階層を表す


def post_detail(request, post_id):
    # pk primarily key
    post = get_object_or_404(Post, pk=post_id)
    # return render(request,'posts/post_detail.html',{'post_id':post_id})
    return render(request, 'posts/post_detail.html', {'post': post})

# Create your views here.
