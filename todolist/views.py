from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core import serializers
import datetime

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'list_todolist': data_todolist,
        'username': request.user,
    }
    return render(request, "todolist.html", context)
    
def get_todolist_json(request):
    todolist = Task.objects.filter(user=request.user).all()
    return HttpResponse(serializers.serialize('json', todolist), content_type="application/json")

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        now = datetime.datetime.now()
        date = now.strftime("%d").rstrip("0")
        month = now.strftime("%B")
        year = now.strftime("%Y")
        date = f"{month} {date}, {year}"

        new_task = Task(user=request.user, date=date, title=title, description=description)
        new_task.save()

        return HttpResponse(serializers.serialize("json", [new_task]), content_type="application/json")

    return HttpResponseNotFound()

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title != "" and description != "":
            now = datetime.datetime.now()
            date = now.strftime("%d").rstrip("0")
            month = now.strftime("%B")
            year = now.strftime("%Y")
            date = f"{month} {date}, {year}"
            Task.objects.create(user=request.user, date=date, title=title, description=description)
            return HttpResponseRedirect(reverse('todolist:show_todolist'))

        messages.info(request, 'Judul atau Deskripsi belum diisi!')

    return render(request, 'createtask.html')