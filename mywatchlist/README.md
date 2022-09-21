# Lab 2 - Dafi Nafidz Radhiyya (2106701564)

[Link Menuju Aplikasi Heroku](http://dafi-lab1-pbp.herokuapp.com/)

## Perbedaan JSON, XML dan HTML

## *Data Delivery*
Seperti yang sudah dipelajari, aplikasi Django yang dibuat dapat memberikan *response* sesuai dengan *client request*. Contohnya, dengan menambahkan *path* `/wishlist` pada [link aplikasi](http://dafi-lab1-pbp.herokuapp.com/), maka akan dikembalikan *response* berupa halaman dalam format HTML. *Response* dalam bentuk halaman HTML tersebut merupakan salah satu contoh data delivery. Selain HTML, terdapat juga format lain seperti XML dan JSON. *Data delivery* tentunya sangat penting dalam pengimplementasian sebuah *platform*. Karena, data merupakan salah satu hal yang mungkin di-*request*.

Selanjutnya, *data delivery* juga memungkinkan *developer* untuk menghemat ruang penyimpanan. Hal ini dikarenakan, biasanya terdapat beberapa *file*/data yang tidak disimpan di server, tapi di-*generate* oleh kode program. Contohnya, adalah implementasi XML dan JSON pada tugas ini. 

## Implementasi
1. Buat django-app mywatchList menggunakan *command* `python3 manage.py startapp mywatchList`.
2. Tambahkan `path('mywatchlist/', include('mywatchlist.urls'))` pada `urlpatterns` di `project_django/urls.py` agar pengguna dapat mengakses http://localhost:8000/mywatchlist.
3. Membuat model MyWatchList dengan menambahkan 
    ```python
    from django.db import models

    class WatchAttr(models.Model):
        watched = models.CharField(max_length=10)
        title = models.CharField(max_length=255)
        rating = models.FloatField()
        release_date = models.TextField()
        review = models.TextField()
    ```
    pada `mywatchlist/models.py`
1. [HTML](http://dafi-lab1-pbp.herokuapp.com/mywatchlist/html)