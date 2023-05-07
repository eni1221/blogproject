from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    blogs=Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def new(request):
    return render(request, 'new.html')


def list(request):
    blogs=Blog.objects
    #User=get_user_model()
    
   # context={
    #    'user':User
   # }
    return render(request,'list.html',{'blogs':blogs})
    #return render(request,'list.html',context)
   
def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    return render(request,'detail.html', {'blog':blog_detail})



def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.writer=request.GET['writer']
    blog.save()
    return redirect('/blog/'+str(blog.id))








