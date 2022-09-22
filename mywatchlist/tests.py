from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestMyWatchList(TestCase):
    def test_html_url_is_exist(self):
        response = Client().get(reverse('mywatchlist:show_mywatchlist'))
        self.assertEqual(response.status_code, 200)

    def test_xml_url_is_exist(self):
        response = Client().get(reverse('mywatchlist:show_xml'))
        self.assertEqual(response.status_code, 200)

    def test_json_url_is_exist(self):
        response = Client().get(reverse('mywatchlist:show_json'))
        self.assertEqual(response.status_code, 200)