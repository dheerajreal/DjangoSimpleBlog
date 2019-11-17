from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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


def detail(request, number, slug=None):
    # the slug isn't used for lookup
    # slugfield is only for SEO-friendly URLs
    blog = get_object_or_404(BlogPost, pk=number)
    context = {
        "blog": blog
    }
    return render(request, "blog/detail.html", context)


def archive(request):
    blogs = BlogPost.objects.order_by('-date_created')
    # pagination
    page_no = request.GET.get('page', 1)
    per_page = 10
    blog_page = Paginator(blogs, per_page)
    try:
        blogs = blog_page.page(page_no)
    except PageNotAnInteger:
        blogs = blog_page.page(1)
    except EmptyPage:
        blogs = blog_page.page(blog_page.num_pages)

    context = {
        "blogs": blogs,
    }
    return render(request, "blog/archive.html", context)


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
