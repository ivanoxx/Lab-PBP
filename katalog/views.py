from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_item': data_barang_katalog,
        'nama': 'Dafi Nafidz Radhiyya',
        'student_id': '2106701564'
    }
    return render(request, "katalog.html", context)
