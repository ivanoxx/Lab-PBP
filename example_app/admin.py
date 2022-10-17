from django.contrib import admin
from katalog.models import CatalogItem
from mywatchlist.models import WatchAttr
from todolist.models import Task

# Register your models here.

admin.site.register(CatalogItem)
admin.site.register(WatchAttr)
admin.site.register(Task)
