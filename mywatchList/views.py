from django.shortcuts import render
from mywatchList.models import WatchAttr
from django.http import HttpResponse
from django.core import serializers

def show_mywatchList(request):
    data_mywatchList = WatchAttr.objects.all()
    context = {
        'mywatch_list': data_mywatchList,
        'nama': 'Dafi',
        'student_id': '2106701564'
    }
    return render(request, "mywatchList.html", context)

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