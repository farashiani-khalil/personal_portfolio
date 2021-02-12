from django.shortcuts import render , get_object_or_404

from .models import Blogs

def show_blogs(request):
    blogs = Blogs.objects.order_by('-date')[:2]
    return render(request,'blog/show_blogs.html',{ 'blogs' : blogs})


def detail(request,blog_id):
    blog = get_object_or_404(Blogs , pk=blog_id)
    return render(request , 'blog/detail.html' , {'blog':blog})
