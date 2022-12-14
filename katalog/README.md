**Link heroku : https://catalogg.herokuapp.com/katalog/**

**Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan penjelasan kaitan antara urls.py, views.py, models.py, dan berkas html;**
![bagan](https://user-images.githubusercontent.com/112618025/190291083-9c06a725-2284-4dc5-b92b-d3b7bc185edd.png)

Views akan menerima request dan mengembalikan respon. Responnya tidak selalu berupa halaman web, bisa berupa gambar, xml, atau dialihkan. Models merupakan sekumpulan data yang disimpan untuk di proses di dalam aplikasi. Models akan memodelkan atau memberikan skema data seperti apa, tetapi bukan databasenya.

Hubungan views.py dan urls.py\
Request dari user akan diekstrak argumennya, seperti /path, /search?=.. sesuai host dan port(s) nya. Selanjutnya, akan dilakukan routing/pemetaan untuk mencari views mana yang menangani argumen tersebut dan request-nya akan diforward ke views tersebut. Cara django memetakannya adalah dengan mencocokkan polanya menggunakan reguler expression. Kemudian, akan dilakukan pengolahan sesuai request yang ada dan dihasilkan respons yang akan dikirim ke client.

Hubungan views.py, urls.py, dan berkas html\
Dari hasil pemrosesan data, ada value tertentu yang selanjutnya digabungkan/merged ke template html yang dibuat sendiri. Sehingga, nantinya akan menjadi satu file html yang utuh kemudian dikirim ke user.

Hubungan views.py, urls.py, models.py, dan berkas html\
Models akan mengambil, menghapus, atau menambahkan data dari database. Misalnya,  views.py ingin meminta data ke models.py. Models akan mengambil data dari database lalu akan diberikan ke views.py. Setelah itu, data yang diberikan tadi akan dilakukan merged atau ditambahkan dengan views.py ke template yang ada di berkas html. Sehingga, akan menjadi halaman html yang utuh yang kemudian menjadi respon ke client.

**Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Virtual environment adalah sebuah environment manager yang digunakan untuk membuat lingkungan virtual yang terisolasi. Virtual environment juga dapat diartikan sebagai lingkungan virtual yang terisolasi dari lingkungan luar yang berarti apapun yang diinstall/dilakukan di dalam lingkungan virtual tidak akan mengganggu aplikasi lain di lingkungan luar.

Virtul environment perlu digunakan agar setiap kali membuat project baru dapat dipastikan kalau versi library uang digunakan di suatu project tidak akan berubah apabila melakukan update di library yang sama pada project lainnya.

Misalnya, saya membuat dua project disaat yang bersamaan, yaitu project A dan project B. Dalam mengerjakan kedua project tersebut, saya memerlukan dua library dengan versi yang berbeda, yaitu library numpy versi 2.0 untuk project A dan library numpy versi 1.0. Jika tidak menggunakan virtual environment, saya harus downgrade numpy ke versi 1.0 untuk mengerjakan project B, tetapi hal ini dapat berdampak ke project A karena project A menggunakan numpy versi 2.0. Dengan menggunakan virtual environment, saya perlu membuat dua environment, yaitu environment A dan environment B yang masing-masing project memiliki versi numpy atau modulnya tersendiri.

Ya, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Akan tetapi, modul yang digunakan akan diambil dari site-packages atau global environment. Sehingga, belum tentu modul yang digunakan sesuai dengan proyek yang kita buat. 

**Cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas**

Pada poin 1, saya akan mengimplementasikan view dasar. Saya membuat fungsi untuk menerima parameter request dan mengembalikan render(request, ??? katalog.html???). Pada poin 2, saya melakukan import fungsi yang sudah saya buat sebelumnya dari katalog.views, menambahkan nama aplikasi, dan membuat urlpatterns yang berisi path pada urls.py di folder katalog. Ketiga hal tersebut saya lakukan untuk melakukan routing terhadap fungsi views. Pada urls.py di project_django, saya menambahkan bagian urlpatterns, yaitu path(???katalog/???, include(???katalog.urls???)).

Selanjutnya, saya melakukan import models dari fungsi views yang sudah saya buat sebelumnya (form katalog.models import CatalogItem). Saya membuat variabel baru bernama data_barang_katalog untuk mengambil semua objek di CatalogItem dengan memanggil CatalogItem.objects.all(). Kemudian, saya membuat context yang berisi list_barang : data_barang_katalog, nama, dan id saya. Terakhir, pada bagian return, saya menambahkan variabel context agar semua variabel di dalam context akan di-render oleh Django juga.\

Pada poin 3, untuk melakukan mapping terhadap data yang di-render pada fungsi views, saya menggunakan sintaks template Django, yaotu {{data}}. Pertama, saya membuka file html dalam direktori katalog lalu mengubah bagian Fill me! Menjadi {{nama}} dan {{id}}. Kemudia, saya juga menambahkan iterasi untuk menampilkan daftar barang ke dalam tabel dengan memanggil nama variabel spesifik dari objek yang ada dalam kontainer.

Pada poin 4, saya menambahkan dua variabel repository secret baru untuk deployment, yaitu HEROKU_API_KEY dengan value API KEY akun hero saya dan HEROKU_APP_NAME dengan value catalogg. Setelah menyimpan dua variabel tersebut, saya langsung menjalankan kembali workflow yang gagal dan status deployment sukses. Terakhir, saya mengakses aplikasi dengan menambahkan /katalog.
