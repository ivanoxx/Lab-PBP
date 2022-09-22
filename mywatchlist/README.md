# Lab 2 - Dafi Nafidz Radhiyya (2106701564)

[Link Menuju Aplikasi Heroku](http://dafi-lab1-pbp.herokuapp.com/mywatchlist)

## Perbedaan JSON, XML dan HTML

1. HTML: HTML merupakan seubah markup language bagi sebuah dokumen untuk ditampilkan pada web. Pada dasarnya, HTML menjadi landasan desain sebuah web-app.
2. XML: Sedangkan, XML merupakan eXtensible markup language. Yang mana biasanya digunakan untuk mengirimkan data tanpa ada tampilan seperti HTML.
3. JSON: JSON kurang lebih memiliki kegunaan yang hampir sama dengan XML, hanya saja memiliki sintaks yang berbeda.

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
4. Data dari objek MyWatchList dapat dimasukkan pada `fixtures/initial_mywatchlist_data.html` dan diisi sesuai dengan *fields*-nya.
5. Untuk menyajikan data tersebut dalam tiga format, yaitu HTML, XML, dan JSON, pertama-tama buat fungsi yang akan mengembalikan *response* berupa XML, JSON, dan HTML. Tambahkan juga fungsi yang dapat mengembalikan *response* data dalam bentuk JSON ataupun XML bila ingin diakses menggunakan id.
6. Selanjutnya, tambahkan  *path*-nya pada `mywatchlist/urls.py`
    ```python 
    ...
    urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    ]
    ...
    ```
7. Untuk deployment, karena saya menggunakan repositori tugas 2 pada tugas kali ini, maka tinggal lakukan `git add`, `commit`, dan `push` maka django-app akan ter-*deploy*.

## Postman 
![html](https://cdn.discordapp.com/attachments/902951430153981993/1022005070717522020/unknown.png)
![xml](https://cdn.discordapp.com/attachments/902951430153981993/1022005115206512740/unknown.png)
![json](https://cdn.discordapp.com/attachments/902951430153981993/1022005197037391922/unknown.png)