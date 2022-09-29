from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import showxml 
from mywatchlist.views import showjson
from mywatchlist.views import show_id_xml
from mywatchlist.views import show_id_json
from mywatchlist.views import show_watched


app_name = 'mywatchlist'

urlpatterns = [
    path('xml/<int:id>', show_id_xml, name='show_id_xml'),
    path('json/<int:id>', show_id_json, name='show_id_json'),
    path('xml/', showxml, name='showxml'),
    path('json/', showjson, name='showjson'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('', show_watched, name='show_watched')
]