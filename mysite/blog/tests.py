from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import BlogPost


class ResponseCodeTest(TestCase):
    def test_home_page_response_code(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_about_page_response_code(self):
        response = self.client.get("/about/")
        self.assertEquals(response.status_code, 200)

    def test_contact_page_response_code(self):
        response = self.client.get("/contact/")
        self.assertEquals(response.status_code, 200)

    def test_archive_page_response_code(self):
        response = self.client.get(reverse("archive"),)
        self.assertEquals(response.status_code, 200)


class BlogModelTest(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(username="hi", password="hi")
        self.blogpost = BlogPost.objects.create(
            title="hi test blog", content="hello")
        return super().setUp()

    def test_blog_count(self):
        blogs = BlogPost.objects.all().count()
        self.assertEqual(blogs, 1)

    def test_blog_slug(self):
        self.assertEqual(self.blogpost.slug(), "hi-test-blog")


class TestExtra(TestCase):
    def setUp(self):
        self.blog = BlogPost.objects.create(title="title", content="content")

    def test_extra(self):
        self.assertEquals(BlogPost.objects.count(), 1)
        self.assertEquals(str(self.blog), "title")
