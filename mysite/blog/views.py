from django.shortcuts import render ,get_object_or_404
# from django.http import HttpResponse
from .models import BlogPost
# Create your views here.


def index(request):
    blogs = BlogPost.objects.order_by('-date_created')[:5]
    context = {
        "blogs": blogs,
    }
    return render(request, "blog/home.html", context)


def detail(request, number):
    blog = get_object_or_404(BlogPost,pk=number)
    context={
        "blog":blog
    }
    return render(request, "blog/detail.html",context)


def archive(request):
    blogs = BlogPost.objects.order_by('-date_created')
    context = {
        "blogs": blogs,
    }
    return render(request, "blog/archive.html",context)


def contact(request):
    return render(request, "blog/contact.html")


def about(request):
    return render(request, "blog/about.html")
