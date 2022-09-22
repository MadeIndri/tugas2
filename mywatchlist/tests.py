from django.test import TestCase
from django.test import Client
#from django.urls import reverse
#from mywatchlist.views import show_mywatchlist, showxml, showjson

# Create your tests here.
class Test(TestCase):
    def test_html(self):
        client = Client()
        #response = client.get(reverse('mywatchlist:show_mywatchlist'))
        response = client.get(('/mywatchlist/html/'))
        self.assertEquals(response.status_code,200)
    
    def test_xml(self):
        client = Client()
        #respon = client.get(reverse("mywatchlist:showxml"))
        response = client.get(('/mywatchlist/xml/'))
        self.assertEquals(response.status_code,200)
    
    def test_json(self):
        client = Client()
        #respon = client.get(reverse("mywatchlist:showjson"))
        response = client.get(('/mywatchlist/json/'))
        self.assertEquals(response.status_code,200)