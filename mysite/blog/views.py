from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("INDEX")


def detail(request,number):
    return HttpResponse(f"DETAIL {number}")


def archive(request):
    return HttpResponse("ARCHIVE")

def contact(request):
    return HttpResponse("CONTACT")


def about(request):
    return HttpResponse("ABOUT")
