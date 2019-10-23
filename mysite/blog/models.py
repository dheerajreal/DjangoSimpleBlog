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
