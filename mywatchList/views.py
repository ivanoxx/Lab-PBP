from django.shortcuts import render
from mywatchList.models import WatchAttr
from django.http import HttpResponse
from django.core import serializers

def show_mywatchList(request):
    data_mywatchList = WatchAttr.objects.all()
    context = {
        'mywatch_list': data_mywatchList,
        'nama': 'Dafi',
        'student_id': '2106701564',
        'message': bonus()
    }
    return render(request, "mywatchList.html", context)

def bonus():
    watched_list = WatchAttr.objects.all().values("watched")
    watched, not_watched = 0, 0
    for w in watched_list:
        if w['watched'] == 'Yes':
            watched += 1
        else:
            not_watched += 1

    if watched >= not_watched:
        return "Selamat, kamu sudah banyak menonton!"
    return "Wah, kamu masih sedikit menonton!"
    
def show_xml(request):
    data = WatchAttr.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchAttr.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = WatchAttr.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchAttr.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")