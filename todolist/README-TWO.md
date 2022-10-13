**Perbedaan Asynchronus Programming dengan Synchronus Programming**

Asynchronous programming merupakan pemrograman yang tidak terikat pada input output (I/O)  protocol. Hal ini menandakan bahwa pemrograman asynchronous tidak melakukan pekerjaannya dengan eksekusi baris program satu persatu secara hirarki. Asynchronous programming melakukan pekerjaannya tanpa harus terikat dengan proses lain atau secara Independent sehingga pemrograman asinkronus memungkinkan suatu tugas berjalan secara bersamaan tanpa harus menunggu tugas sebelumnya selesai. 

Synchronous programming memiliki pendekatan tugas akan dieksekusi satu persatu sesuai dengan urutan dan prioritas tugas. Hal ini memiliki kekurangan pada lama waktu eksekusi karena masing-masing tugas harus menunggu tugas lain selesai untuk diproses terlebih dahulu.

**Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**

Event driven programming adalah suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event/peristiwa yang merupakan keluaran atau tindakan pengguna, atau bisa berupa pesan dari program lainnya. Salah satu contoh penerapan pada tugas ini adalah pada bagian create task di bagian modal. Jika button submit di-click oleh user, maka function ajax akan dijalankan. Jika button submit tidak di-click, function ajax tidak akan dijalankan.

**Jelaskan penerapan asynchronous programming pada AJAX**

Penerapan asynchronus pada ajax terjadi saat user menambahkan data, website akan melakukan update data tanpa harus merefresh halaman tersebut. Contohnya saat user melakukan event driven programming, ajax akan menampung data dan mengirimkan data ke server secara asynchronus. Transfer data terjadi ke server web pada background. Ketika method POST selesai dieksekusi, program akan langsung memanggil fungsi add_ajax pada views. Pada tugas ini, dapat dilihat ketika user menambahkan task baru, maka akan terbentuk card yang langsung muncul tanpa harus mereload halaman.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
1. Membuat function show_json di views.py untuk menampilkan data json
2. Membuat routing di urls.py
3. Menambahkan navbar dan modal untuk membuat input create task
4. Membuat script jquery untuk melakukan get data dari json. Lal,  loop tiap elemennya dan dimasukkan ke elemen cards.
5. Membuat function add_ajax di views yang nantinya akan digunakan untuk melakukan post
6. Membuat function post yang akan diakses melalui event click pada button. Pada function ini, akan dibuat objek task baru dan dimasukkan ke cards