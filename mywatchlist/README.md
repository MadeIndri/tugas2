**Link heroku app : https://mywatchlistt.herokuapp.com/mywatchlist/html/, https://mywatchlistt.herokuapp.com/mywatchlist/json/, https://mywatchlistt.herokuapp.com/mywatchlist/xml/**

**Perbedaan antara JSON, XML, dan HTML**

JSON singkatan dari JavaScript Object Nation adalah sebuah format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna dan dapat diakses secara logis. JSON disebut sebagai bahasa ideal untuk pertukaran data antar apliksi karena dapat dibaca dengan berbagai macam bahasa pemrograman, C, C++, Java, JavaScript, Python, dan masih banyak lagi. JSON terdiri dari dua struktur, yaitu kumpulan value yang saling berpasangan (object) dan kumpulan value yang berurutan (array).

XML singkatan dari Extensive Markup Language adalah sebuah markup language yang dirancang untuk menyimpan dan mengantarkan data antar server. Hal ini karena ada keunikan dan perbedaan sistem yang digunakan oleh setiap server yang terhubung ke internet. XML akan menyimpan data dalam format teks sederhana. Sehingga, data dapat dimengerti oleh server yang menerima data tanpa perlu modifikasi apapun.

HTML singkatan dari Hypertext Markup Language adalah bahasa standar pemrogaman yang digunakan untuk membuat halaman website, yang diakses melalui internet.

Perbedaan JSON dan XML\
Hal pertama yang membedakan adalah cara menyimpan elemennya. JSON menyimpan elemennya secara efisien, tetapi tidak rapi untuk dilihat. XML menyimpan elemennya dengan cara yang terstruktur, mudah dibaca oleh manusia dan mesin, tetapi kurang efisien.

Hal kedua yang membedakan adalah ekstensi file. JSON diakhirid engan ekstensi .json, sedangkan XML diakhiri dengan ekstensi .xml. Hal ketiga yang membedakan adalah penerapannya. JSON digunakan untuk mengirimkan data dengan menguraikan data dan mengirimkannya melalui internet. XML memiliki data yang lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan.

Dalam hal fitur, JSON melakukan penguraian lebih cepat karena didukung oleh mesin JavaScript karena itu transfer datanya lebih cepat. XML rumit dan lambat dalam penguraian karena itu transmisi data lebih lambat. Dalam hal penyimpanan data juga berbeda, JSON menyimpan data seperti peta dan XML menyimpan data seperti struktur pohon.

Perbedaan JSON, XML, dan HTML\
JSON dan XML memiliki fungsi yang berbeda dengan HTML. XML dan JSON kurang lebih memiliki fungsi yang sama, yaitu untuk menyimpan dan mengirimkan data. Sedangkan, HTML berfungsi untuk menampilkan data.

**Alasan memerlukan data delivery dalam pengimplementasian sebuah platform**

Dalam pembuatan sebuah platform, kita perlu mengirimkan data dari satu stack ke stack lainnya. Data yang dikirimkan tidak tentu dalam bentuk yang sama, bisa saja bentuknya berbeda (bermacam-macam). Format data yang banyak digunakan diantaranya html, xml, dan json.

**Cara saya mengimplementasikan checklist di atas**

Pertama-tama, saya membuat aplikasi baru bernama mywatchlist dengan perintah pyhton manage.py startapp mywatchlist. Kemudian, saya menambahkan mywatchlist di bagian installed_apps yang ada di settings.py folder project_django. Saya membuat models dengan nama MyWatchList yang berisi kelima atribut yang disebutkan yang dilanjutkan dengan melakukan makemigrations dan migrate. Selanjutnya, saya menambahkan 10 data di dalam berkas initial_mywatchlist_data.json dalam folder fixtures mywatchlist dan melakukan load berkas tersebut.

Langkah selanjutnya, saya mengimplementasi views dasar. Pertama, saya membuat fungsi show_mywatchlist dengan parameter request dan mengembalikan render (request, ???mywatchlist.html) dan membuat berkas mywatchlist.html di dalam folder tempates mywatchlist. Kemudian, saya membuat berkas urls.py untuk melakukan routing terhadap fungsi viewa yang sudah dibuat sebelumnya. Terakhir, saya menambahkan path pada variabel urlpattern di berkas urls.py pada folder project_django.

Langkah selanjutnya, saya akan mengubungkan models dengan views dan template. Saya meng-import models ke dalam views.py dan menambahkan kode untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel. Lalu, menambahkan variabel context pada pengembalian fungsi render. Paada berkas html, menambahkan tag nama dan id serta membuat perulangan untuk menampilkan 10 data yang sudah dibuat sebelumnya.

Selanjutnya, saya mengembalikan data dalam tiga bentuk yang diminta, yaitu HTML,XML, dan JSON. Pertama, saya membuat fungsi yang bernama showxml dan showjson yang menerima parameter request di berkas views.py pada folder mywatchlist. Kemudian, melakukan import HttpResponse dan Serializer pada bagian paling atas dan membuat variabel data yang menyimpan hasilquery dari seluruh data yang ada pada MyWatchList. Kemudian, saya menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisai menjadi XML ataupun JSON dan parameter content_type = ???application/xml??? atau ???application/json???. Terakhir, saya melakukan import fungsi yang sudah dibuat pada berkas urls.py dan menambahkan path url dalam urlpatterns untuk mengakses fungsi yang sudah diimpor sebelumnya. Hal yang sama juga saya lakukan untuk mengembalikan data berdasarkan ID, yang membedakan hanya perlu menambahkan .filter(pk=id) pada variabel data dan  /<int:id> pada path url. Untuk yang menampilkan html, saya mengubah path yang awalnya ??? ??? menjadi ???html/???.

Langkah terakhir, saya menambahkan unit test pada test.py dengan melakukan import TestCase dan Client. Kemudian, membuat tiga fungsi untuk mengetest ketiga format.

Saya juga mengerjakan bagian bonus dengan menambahkan if-else di dalam fungsi show_mywatchlist dan menambahkan context output untuk menampilkannya dalam bentuk html. Begitu pula pada baerkas html, saya menambahkan baris baru untuk output.

**Screenshot Postman**\
**HTML**
![html1n](https://user-images.githubusercontent.com/112618025/191658610-18eac20f-a7fd-4c16-8290-3f4cd58ad312.jpg)
![html2](https://user-images.githubusercontent.com/112618025/191658615-b2c39e11-f8d9-40df-ae09-0db73d2b9731.jpg)
![html3](https://user-images.githubusercontent.com/112618025/191658614-df1abc64-2ef1-4b34-82ea-e14f6184fd56.jpg)
**XML**
![xml1](https://user-images.githubusercontent.com/112618025/191658774-db76752b-ca3f-4f1c-8fba-8fb75c72905a.jpg)
![xml2](https://user-images.githubusercontent.com/112618025/191658764-39c136cc-424c-4383-aa77-b1c643fa6870.jpg)
**JSON**
![json1](https://user-images.githubusercontent.com/112618025/191658831-a6e04c29-aea6-48ce-9341-62a2ce4c0574.jpg)
![json2](https://user-images.githubusercontent.com/112618025/191658826-24920bd4-7795-4f19-9102-436b2c6c13f3.jpg)
