## Perbedaan *Asynchronous Programming* Dengan *Synchronous Programming*
Pada *synchronous programming*, bila terjadi sebuah *event*, *user* harus menunggu hingga halaman memberikan *response*. Sedangkan pada *asynchronous programming*, *user* tetap bisa beraktivitas biasa sekalipun terjadi sebauh *event*. *Response* akan langsung ditampilkan ketika sudah selesai diproses.

## *Event-Driven Programming*
Merupakan sebuah paradigma yang mana jalannya program dipengaruhi oleh *event* yang terjadi. Program akan menjalankan perintah tergantung dari jenis *event*-nya. Salah satu contoh implementasinya pada tugas ini adalah penggunaan method `click` pada tombol `submit` untuk menambahkan *task*. Artinya, ketika tombol `submit` ditekan, akan ada beberapa perintah yang dijalankan program, seperti membuat objek *task* baru itu sendiri dan melakukan *refresh* secara asinkronus.

## Penerapan *Asynchronous Programming* Pada AJAX
Dengan memanfaatkan AJAX, *request* dari *user* tidak akan menghalangi aktivitas yang sedang berjalan pada sebuah halaman. Lebih jelasnya, halaman tidak melakukan *reload* yang akan memberhentikan semua aktivitas secara sementara hingga *response* diberikan.

## Implementasi
1. AJAX GET
   + Membuat *view* untuk mengembalikan semua data *task* dalam bentuk JSON.
        ```python
        def get_todolist_json(request):
            todolist = Task.objects.filter(user=request.user).all()
            return HttpResponse(serializers.serialize('json', todolist), content_type="application/json")
        ```
   + Menambahkan path `/todolist/json` pada `/todolist/urls.py` dengan *view* di atas.
   + Pengambilan *task* menggunakan *method* `get` dari jQuery.
        ```js
        $.get("/todolist/json", showCards);
        ```
     Fungsi `showCards` digunakan untuk menampilkan data yang sudah diambil dalam bentuk *card*.
2. AJAX POST
    + Memodifikasi tombol `Tambah Task Baru` sehingga menampilkan modal.
    + Buat *view* (`add_task`) untuk menerima data yang di-*submit* pada modal.
    + Gunakan method `post` dari jQuery untuk mengupdate *task* baru secara asinkronus.
        ```js
        $.post(
          "{% url 'todolist:add_task' %}",
          {
            title: $("#title").val(),
            description: $("#description").val(),
            csrfmiddlewaretoken: "{{ csrf_token }}"
          },
          function() {
            $.get("/todolist/json", showCards)
          },
          "json"
        );
        ```