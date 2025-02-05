from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget

from .models import BlogPost, Comment, ContactFormEntry

# change admin interface
admin.site.index_title = "Blog admin"
admin.site.site_header = "Blog admin"
admin.site.site_title = "Blog admin"
admin.site.site_url = "/"


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ['comment', 'name', 'date_created', ]
    exclude = ["email"]
    verbose_name = "comment"
    extra = 0


class BlogPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    # things to on admin page
    list_display = ("title", "date_created", "date_updated")
    # can filter by date_created
    list_filter = ["date_created"]
    # allow search
    search_fields = ["title", "content"]
    inlines = [CommentInline, ]


class ContactFormEntryAdmin(admin.ModelAdmin):
    # things to on admin page
    list_display = ("name", "email", "message", "date_created")
    # can filter by date_created
    list_filter = ["date_created"]


# admin.site.register(Comment)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(ContactFormEntry, ContactFormEntryAdmin)
