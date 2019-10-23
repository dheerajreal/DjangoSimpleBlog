from django.contrib import admin
from .models import BlogPost
# Register your models here.

# change admin interface
admin.site.index_title = "Blog admin"
admin.site.site_header = "Blog admin"
admin.site.site_title = "Blog admin"
admin.site.site_url = "/blog"

class BlogPostAdmin(admin.ModelAdmin):
    # things to on admin page
    list_display = ("title", "date_created", "date_updated")
    # can filter by date_created
    list_filter = ["date_created"]
    # allow search
    search_fields = ["title", "content"]


admin.site.register(BlogPost, BlogPostAdmin)
