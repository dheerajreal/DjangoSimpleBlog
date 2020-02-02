from django.test import TestCase


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
        response = self.client.get("/archive/")
        self.assertEquals(response.status_code, 200)
