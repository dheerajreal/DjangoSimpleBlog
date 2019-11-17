from django.contrib import admin
from .models import BlogPost, ContactFormEntry
# Register your models here.

# change admin interface
admin.site.index_title = "Blog admin"
admin.site.site_header = "Blog admin"
admin.site.site_title = "Blog admin"
admin.site.site_url = "/"


class BlogPostAdmin(admin.ModelAdmin):
    # things to on admin page
    list_display = ("title", "date_created", "date_updated")
    # can filter by date_created
    list_filter = ["date_created"]
    # allow search
    search_fields = ["title", "content"]


class ContactFormEntryAdmin(admin.ModelAdmin):
    # things to on admin page
    list_display = ("name", "email", "message", "date_created")
    # can filter by date_created
    list_filter = ["date_created"]


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(ContactFormEntry, ContactFormEntryAdmin)
