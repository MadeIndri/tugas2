**Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**

**Internal CSS** adalah kode CSS yang ditulis di dalam tag style dan kode HTML dituliskan di bagian head file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain. Dengan kata lain, Internal CSS dipakai jika ingin tampilan website yang berbeda pada setiap halamannya.

Kelebihan : 
Perubahan hanya berlaku pada satu halaman saja.
Tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file.
Class dan ID bisa digunakan oleh internal stylesheet.

Kekurangan :
Tidak efisien jika ingin menggunakan CSS yang sama untuk beberapa file sekaligus.
Performa website lebih lama karena akan melakukan loading ulang setiap ganti halaman.
Ukuran file HTML menjadi lebih besar karena setiap halaman mengandung CSS nya sendiri.

**Eksternal CSS** adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS dengan menyertakan referensi ke file HTML di dalam elemen link biasanya diletakkan setelah bagian head pada halaman. File eksternal tersebut tidak boleh berisi tag HTML apa pun. Dengan menggunakan, eksternal CSS dapat mengubah seluruh tampilan website hanya dengan mengubah satu file.

Kelebihan :
•	Ukuran file HTML lebih kecil dan struktur html lebih rapi.
•	Performa lebih cepat
•	File CSS dapat digunakan oleh beberapa halaman website sekaligus.

Kekurangan :
•	Jika gagal memanggil file CSS ke dalam file HTML, tampilan website akan berantakan.

**Inline CSS** adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, inline CSS akan ditulis pada atribut tersebut. 

Kelebihan:
•	Membantu ketika ingin melihat perubahan pada satu elemen HTML.
•	Memperbaiki kode dengan cepat.
•	Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.
•	Tidak perlu membuat file tambahan.

Kekurangan :
•	Tidak efisien karena setiap tag HTML harus memiliki style masing-masing.
•	Sulit jika ingin mengikuti, menggunakan kembali, dan menskalakan CSS.
•	Tidak dapat menata elemen semu, speerti hover atau link colors.

**Jelaskan tag HTML5 yang kamu ketahui.**

•	Tag html: sebagai root, semua tag dalam <html> merupakan isi dari dokumen HTML
•	Tag head : di dalamnya berisi informasi tentang penulis, judul dokumen, kata kunci, dll, berada pada bagian atas HTML.
•	Tag body: isi dari dokumen yang akan ditampilkan pada website
•	Tag title : judul dokumen HTML
•	Tag link : menghubungkan halaman dengan sumber luar
•	Tag style : untuk tampilan konten (biasanya dengan CSS) biasanya dalam bagian head dokumen
•	Tag p : membuat sebuah paragraf
•	Tag a : membuat hyperlink
•	Tag h[1-6] : heading HTML
•	Tag div : menentukan bagian dalam dokumen
•	Tag span : memasukkan inline style dalam dokumen
•	Tag br : memberikan space baris
•	Tag hr : membuat garis horizontal
•	Tag strong : teks cetak tebal
•	Tag em : teks cetak miring
•	Tag code : kode
•	Tag cite : membuat teks miring untuk menyebut judul karya
•	Tag del : memberi garis pada teks
•	Tag ins : menggaris bawahi teks
•	Tag sub dan sup : teks subscript dan superscript
•	Tag bdo : mengganti arah teks
•	Tag ol : ordered list
•	Tag ul : unordered list
•	Tag li : item sebuah list
•	Tag dl : deskripsi list
•	Tag dt : mendefinisikan item di dalam deskripsi list
•	Tag dd : definisi istilah dalam deskripsi list
•	Tag form : membuat form untuk input user
•	Tag fieldset : menyatukan beberapa kolom form dalam satu kategori
•	Tag legend : memberi judul fieldset
•	Tag label : membuat daftar opsi berbentuk checkbox
•	Tag input : input control
•	Tag select : membuat drop-down list
•	Tag optgroup : membuat teks cetak tebal yang digunakan untuk mengklasifikasikan item dalam drop-down box
•	Tag option : membuat item dalam drop-down list
•	Tag textarea : membuat kolom form dengan kapasiatas tak terbatas
•	Tag button : tombol yang bisa diklik
•	Tag table : tabel
•	Tag caption : memberi judul suatu tabel
•	Tag thead, tbody, dan tfoot : header, body, dan footer tabel
•	Tag colgroup : mengkategorikan satu atau lebih kolom tabel
•	Tag col : menentukan atribut value untuk satu atau lebih kolom tabel
•	Tag tr : baris tabel
•	Tag th dan td : membuat cell header dan cell biasa
•	Tag img : gambar
•	Tag map : gambar dengan bagian yang dapat diklik user
•	Tag area : bagian gambar yang dapat diklik
•	Tag object : objek multimedia yang disematkan pada halaman
•	Tag param : parameter untuk mengontrol objek multimedia
•	Tag article : artikel
•	Tag audio : menyematkan suara atau audio dalam dokumen html
•	Tag bdi : merepresentasikan teks yang diisolasi dari sekitarnya untuk tujuan pemformatan teks dua arah
•	Tag canvas : mendefinisikan wilayah dalam dokumen untuk menggambar grafik melalui scripting
•	Tag header : header dokumen atau suatu bagian
•	Tag hgroup : grup header
•	Tag keygen : kontrol untuk public-private pasangan kunci
•	Tag main : main atau konten yang dominan dalam suatu dokumen
•	Tag nav : bagian link navigasi
•	Tag template : fragmen HTML yang harus disembunyikan saat halaman dimuat, tetapi dapat dikloning dan dimasukkan ke dalam dokumen oleh JavaScript.
•	Tag time : menampilkan waktu dan/atau tanggal
•	Tag figure : menghubungkan keterangan bersama-sama dengan beberapa konten tertanam, seperti gambar atau video
•	Tag section : dokumen atau aplikasi bagian generik, dapat digunakan dengan h[1-6] untuk menunjukkan struktur dokumen
•	Tag aside : gambaran dari sebagian konten yang berhubungan dengan isi halaman
•	Tag header : bagian kepala dokumen
•	Tag footer : bagian catatan kaki yang dapat berisi informasi tentang penulis, informasi hak cipta, dll
•	Tag !—komentar-- : untuk memberikan komentar, sehingga tidak adakn terlihat pada web browser ketika dijalankan

**Jelaskan tipe-tipe CSS selector yang kamu ketahui**

1.	Selektor tag atau Type selector : selektor ini akan memilih elemen berdasarkan nama tag. Misal, p { color : white; }, artinya pilih semua elemen dengan tag p, lalu ubah warnanya menjadi putih.
2.	Selektor class : selektor ini akan memilih elemen berdasarkan nama class yang diberikan. Selektor ini ditandai dengan tanda titik di depannya. Misal, .form { color : black ; padding : 5px;}, artinya selektor classnya adalah ‘.form’ dan semua elemen yang memiliki class .form akan diterapkan tampilan tersebut. Sebuah elemen html dapat menggunakan satu atau lebih class, jika ingin menggunakan dua class diberikan spasi daintara dua nama class.
3.	Selektor id : sama dengan selektor class, tetapi id bersifat unik (hanya boleh digunakan oleh satu elemen saja). Selektor ini ditandai dengan tanda pagar (#) di depannya. Misal, #header { background : pink; height : 100px;}, artinya elemen yang memiliki id=header akan diterapkan tampilan tersebut.
4.	Selektor atribut : selektor yang memiliki elemen berdasarkan atribut, hampir sama dengan selektor tag. Misal, input[type=text]{….}, artinya akan memilih elemen <input> yang memiliki atribut type=text.
5.	Selektor universal : selektor untuk menyeleksi semua elemen pada jangkauan(scope) tertentu. Selektor ini ditandai dengan tanda *. Selektor ini biasnaya digunakan untuk me-reset CSS (menghilangkan padding dan margin). Misal, *{ border: 1px solid grey;}, artinya semua elemen memiliki garis solid dengan ukuran 1px dan berwarna abu-abu.
6.	Pseudo selektor : selektor untuk memilih elemen semu, seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagianya. Terdapat dua amacam pseudo selektor, sebagai berikut:
1)	Pseudo-class : selektor untuk state elemen, seperti saat elemen diklik, saat disentuh, dll. Penulisannya menggunakan titik dua setelah elemen. Misal, a:hover{color : green;}, a sebagai selektor dan hover sebagai pseudo class. Artinya, elemen <a> akan diberikan warna hijau saat di-hover atau disentuh pointer. Selektor pseudo-class lainnya, diantaranya : link (untuk memilih link yang belum dikunjungi), visited (untuk memilih link yang sudah dikunjungi), active(untuk memilih elemen yang sedang aktif, seperti saat diklik), fokus(untuk memilih elemen yang sedang dalam keadaan aktif, seperti saat teks diinput), checked(untuk memilih elemen yang dicentang pada checkbox), fullscreen (untuk menampilkan dalam mode layar penuh), enabled (mewakili elemen user interface yang berada dalam status aktif), dll.
2)	Pseudo-element : selektor untuk elemen semu di html. Selektor ini ditandai dengan tanda titik dua ganda (::). Misal, p::first-line{…} untuk memberikan tampilan pada baris pertama elemen p. Contoh selektor pseudo-element, diantaranya : before (untuk memilih elemen semu sebelum elemen), after (untuk emmilih elem semu setelah elemen), marker (untuk emmeilih marker pada list), placeholder (untuk memilih teks placeholder pada elemen input teks), selection, backdrop, dll.
