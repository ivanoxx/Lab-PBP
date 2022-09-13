# Lab 1 - Dafi Nafidz Radhiyya (2106701564)

[Link Menuju Aplikasi Heroku](http://dafi-lab1-pbp.herokuapp.com/)

## Bagan Django *Request & Response Cycle*
---
![Bagan Django *Request & Response Cycle*](https://cdn.discordapp.com/attachments/902951430153981993/1019066428806144081/unknown.png)
1. *Client* mengirimkan *request* dan akan diproses oleh `urls.py` yang bertugas sebagai URL *router*.
   ```python
   urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls')),
   ]
   ```
   URL yang di-*request* akan dicocokkan dengan yang ada pada `urlpatterns`.
2. Setelah dicocokkan, maka akan diteruskan ke `views.py` sesuai dengan fungsi *views* yang dipanggil.
3. Kalau ada aktivitas yang melibatkan *database*, *views* akan memanggil *query* ke `models.py`.
4. Kemudian, akan diteruskan ke *database* untuk memproses data yang dibutuhkan.
5. Selanjutnya, *response* data berupa hasil *query* akan diberikan ke *views*.
6. *Views* kemudian akan memilih `html` yang sesuai dengan yang telah dipetakan sebelumnya.
7. *Response* diberikan kepada *client* berupa `html` dari URL yang di-*request*.

## Penggunaan *Virtual Environment*
---
Setiap aplikasi/proyek Django kemungkinan besar akan membutuhkan *packages* atau *libraries* eksternal yang harus diinstal terlebih dahulu. Proyek Django yang berbeda terkadang membutuhkan *packages* dengan versi yang berbeda juga. Untuk memudahkan pengelolaan masing-masing proyek Django yang berbeda, kita bisa memanfaatkan *virtual environment*. Dengan menggunakan *virtual environment*, artinya kita membuat *environment* berbeda yang terisolasi dari *environment* lainnya. Dengan ini, perubahan yang dilakukan pada sebuah proyek Django tidak akan mempengaruhi proyek lainnya. Maka dari itu, setiap proyek Django lebih baik memiliki *virtual environment*-nya masing-masing. 

Akan tetapi, proyek Django tentu tetap bisa dibangun tanpa menggunakan *virutal environment*. Hanya saja, akan sulit ketika terdapat banyak proyek dalam sebuah *environment*.Seperti yang sudah dikatakan sebelumnya, penggunaan *virtual environment* adalah agar kita lebih mudah mengelola proyek Django yang berbeda secara independen. 

## Implementasi
---
1. Buat fungsi `show_katalog(request)` pada [`views.py`](katalog/views.py). 
   ```python
   def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_item': data_barang_katalog,
        'nama': 'Dafi Nafidz Radhiyya',
        'student_id': '2106701564'
    }
    return render(request, "katalog.html", context)
   ```
   Data dari model diambil pada 
   ```python 
   data_barang_katalog = CatalogItem.objects.all()
   ```
   Data tersebut kemudian akan dikembalikan ke dalam HTML. Hal ini dapat dilihat dari *return value* fungsi di atas.
2. Untuk memetakan fungsi pada `views.py`, akan dibuat sebuah *routing* di `urls.py` baik pada [katalog](katalog) dan [project_django](project_django).
   + Tambahkan   
     ```python
     path('katalog/', include('katalog.urls'))
     ```
     pada `urlpatterns` di `urls.py` di [project_django](project_django) 
   + Tambahkan    
     ```python
     path('', show_katalog, name='show_katalog')
     ```
     pada `urlpatterns` di `urls.py` di [katalog](katalog) 

   Dengan ini, ketika terdapat *client request* terhadap URL `katalog`, fungsi `show_katalog(request)` akan dipanggil.
3. Untuk memetakan data yang didapatkan ke dalam HTML, dapat dimanfaatkan `context` dari fungsi `show_katalog(request)` menggunakan sintaks Django seperti pada tutorial.
4. Untuk deployment, buat aplikasi terlebih dulu pada heroku. Kemudian tambahkan *repository* secret dengan pasangan nama aplikasi dan API key seperti pada tutorial. Selanjutnya lakukan `add`, `commit`, `push` dan aplikasi akan ter-*deploy*


