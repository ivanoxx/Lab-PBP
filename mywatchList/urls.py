from django.urls import path
from mywatchList.views import show_mywatchList, show_xml, show_json, show_json_by_id, show_xml_by_id

app_name = 'mywatchList'

urlpatterns = [
    path('', show_mywatchList, name='show_mywatchList'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]