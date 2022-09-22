from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse

# Create your views here.

def show_mywatchlist(request):
    data_film_mywatchlist = MyWatchList.objects.all()
    watched = 0
    unwatched = 0
    output = " "

    for film in data_film_mywatchlist:
        if (film.watched == True):
            watched += 1
        else:
            unwatched += 1
    
    if (watched >= unwatched):
        output = "Selamat, kamu sudah banyak menonton!"
    else:
        output = "Wah, kamu masih sedikit menonton!"
    context = {
        'list_film': data_film_mywatchlist,
        'nama': 'Made Indri Maharani Natiadewi',
        'id': '2106704295',
        'output': output
    }
    return render(request, "mywatchlist.html", context)

def showxml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def showjson(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_id_xml(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_id_json(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")