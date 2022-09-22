from django.test import TestCase
from django.test import Client

# Create your tests here.
class Test(TestCase):
    def test_html(self):
        client = Client()
        response = client.get(('/mywatchlist/html/'))
        self.assertEquals(response.status_code,200)
    
    def test_xml(self):
        client = Client()
        response = client.get(('/mywatchlist/xml/'))
        self.assertEquals(response.status_code,200)
    
    def test_json(self):
        client = Client()
        response = client.get(('/mywatchlist/json/'))
        self.assertEquals(response.status_code,200)