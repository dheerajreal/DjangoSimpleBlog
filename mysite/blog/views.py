from django.shortcuts import render
# from django.http import HttpResponse
from .models import BlogPost
# Create your views here.


def index(request):

    blogs = BlogPost.objects.order_by('-date_created')
    context = {
        "blogs": blogs,
    }
    return render(request, "blog/home.html", context)


def detail(request, number):
    return render(request, "blog/detail.html")


def archive(request):
    return render(request, "blog/archive.html")


def contact(request):
    return render(request, "blog/contact.html")


def about(request):
    return render(request, "blog/about.html")
