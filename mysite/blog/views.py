from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
# Create your views here.


def index(request):

    blogs=BlogPost.objects.order_by('-date_created')
    context={
        "blogs":blogs,
        }
    return render(request,"blog/home.html",context)


def detail(request,number):
    return HttpResponse(f"DETAIL {number}")


def archive(request):
    return HttpResponse("ARCHIVE")

def contact(request):
    return render(request,"blog/contact.html")


def about(request):
    return render(request,"blog/about.html")
