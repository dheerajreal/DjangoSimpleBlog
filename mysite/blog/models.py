from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=256)

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title


class Comment(models.Model):
    on_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ContactFormEntry(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Contact Form Received "
        verbose_name_plural = "Contact Forms Received "
