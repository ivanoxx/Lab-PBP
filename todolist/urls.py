from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('add/', add_task, name='add_task'),
    path('create-task/', create_task, name='create_task'),
    path('json/', get_todolist_json, name='get_todolist_json'),
    path('register', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]