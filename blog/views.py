from django.shortcuts import render

from .models import Blogs

def show_blogs(request):
    blogs = Blogs.objects.order_by('-date')[:2]
    return render(request,'blog/show_blogs.html',{ 'blogs' : blogs})
