from django.shortcuts import render ,get_object_or_404
# from django.http import HttpResponse
from .models import BlogPost
from .forms import ContactForm
# Create your views here.


def index(request):
    blogs = BlogPost.objects.order_by('-date_created')[:5]
    context = {
        "blogs": blogs,
    }
    return render(request, "blog/home.html", context)


def detail(request, number,slug=None):
    # the slug isn't used for lookup
    # slugfield is only for SEO-friendly URLs
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
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
            "message": "Submitted Successfully",
        }
        return render(request, "blog/contact.html", context)
    context = {
        "form": form,
    }
    return render(request, "blog/contact.html", context)


def about(request):
    return render(request, "blog/about.html")
