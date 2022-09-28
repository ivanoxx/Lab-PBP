# Lab 3 - Dafi Nafidz Radhiyya (2106701564)

[Link Menuju Aplikasi Heroku](http://dafi-lab1-pbp.herokuapp.com/todolist)

## Kegunaan `{% csrf_token %}` Pada Elemen `<form>`
CSRF token digunakan untuk menghindari terjadinya CSRF *attack*. Pada CSRF, *attacker* mengirimkan *form* yang berisi bukan berasal dari server dan biasanya berisi *malicious code*. Django sendiri sudah memiliki *built-in protection* terhadap CSRF *attack*, yaitu salah satu parameter `MIDDLEWARE` di `settings.py`. Ketika sebuah *form* dikirim ke server, maka `{% csrf_token %}` pada elemen `<form>` akan mengecek apakah *form* tersebut memang berasal dari server. Bila valid, maka fungsi pada atribut `action` di elemen `<form>` baru akan dieksekusi. 

## Membuat Elemen `<form>` Secara Manual
Tanpa menggunakan *generator* seperti `{{ form.as_table }}`, elemen `<form>` tetap dapat dibuat secara manual. Beberapa contohnya adalah *form* login (`login.html`) dan tambah task baru (`createtask.html`). Pada `createtask.html` bagian untuk meng-*input* (`<input>` tag) judul dan deskripsi dibuat secara manual. Hal yang harus diperhatikan adalah *value* dari atribut *name* yang harus sesuai dengan kode di server Django.

## Proses Alur Data Dari Submisi *Task* Baru
Pertama, setelah pengguna mengeklik tombol *submit*, data yang sudah di-*input* akan dikirim ke server. Kemudian, data akan diproses oleh fungsi pada `views.py` dan dibuat model objeknya pada menggunakan `Model.objects.create()` untuk disimpan di *database*. Data yang disimpan dapat diakses oleh `views.py` sesuai dengan *logged in user*. Kemudian, *response* akan diberikan berupa data yang sudah di-*render* dalam halaman HTML. 

## Implementasi
1. Gunakan command `python3 manage.py startapp todolist` untuk membuat aplikasi `todolist`. Tambahkan juga `todolist` pada `INSTALLED_APPS` di `/project_django/settings.py`.
2. Tambahkan `path('todolist/', include('todolist.urls')),` pada `urlpatterns` di `/project_django/urls.py`, kemudian buat `urls.py` pada `/todolist`.
    Fungsi `show_todolist` dibuat pada `/todolist/views.py` untuk menampilkan halaman utama `todolist`.
3. Tambahkan kode di bawah ini pada `/todolist/models.py`
    ```python
    from django.db import models
    from django.contrib.auth.models import User

    class Task(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.TextField()
        title = models.CharField(max_length=255)
        description = models.TextField()
    ```
4. Sesuai dengan tutorial, buat fungsi pada `/todolist/views.py` yang meng-*handle* registrasi, *login*, dan *logout*. Buat juga *template* untuk *login form* dan registrasi. Tambahkan `@login_required(login_url='/todolist/login/')` di atas fungsi `show_todolist` agar login harus dilakukan terlebih dahulu sebelum mengakses halaman utama `todolist`.
5. Buat `todolist.html` pada `/todolist/templates`.
6. Membuat `createtask.html` pada `/todolist/templates`. Isinya kurang lebih mirip dengan `login.html`. Buat juga fungsi pada `/todolist/views.py` yang akan meng-*handle* submisi *task* baru.
7. Menambahkan 
    ```python
    from django.urls import path
    from todolist.views import *

    app_name = 'todolist'

    urlpatterns = [
        path('', show_todolist, name='show_todolist'),
        path('create-task/', create_task, name='create_task'),
        path('register', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
    ]
    ```
    pada `/todolist/urls.py`.