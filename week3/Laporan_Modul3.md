# Laporan Praktikum Jaringan Komputer
**Nama:** Niko Rajani Syahputra
**NIM:** 103072400167
**Modul:** 1 & 2 (Instalasi & Pengenalan Tools Wireshark)

## 1. Pendahuluan
Pada Praktikum modul 3 ini, kita akan mencoba menggunakan wireshark untuk mempelajari protokol yang sedang berjalan. Di sini kita akan fokus mempelajari protokol HTTP dan beberapa aspeknya seperti:
<br>
a. GET/RESPONSE HTTP
<br>
b. HTTP Message Format
<br>
c. Retrieving large HTML file
<br>
d. retrieving HTML file with embedded objects
<br>
e. HTTP authentication and security
<br>

Mari kita mulai dari yang pertama

## A. Basic GET/RESPONSE HTTP
Disini kita melihat basic dari get (request ke server untuk meminta data (HTML ATAU JSON)) dan response (response dari server dengan memberikan datanya). 
<br> 
Langkah Langkah yang diperlukan cukup sederhana, yaitu:
<br>
1. Buka wireshark -> Wifi(jika pakai wifi), maka tampilan awalnya akan seperti ini:(Masukkan Gambar)
2. Buka link : http://gaia.cs.umass.edu/wireshark-labs/HTTPwireshark-file1.html di browser anda.
3. Tunggu hasilnya di Wireshark, jika sudah muncul protokol HTTP, kita bisa langsung filter dengan cara ketik http di search/pencarian
<br>

 <p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week2/aset/FIlter%20HTTP(Gambar1).jpeg" alt="Arsitektur Packet Sniffer">
  <br>
</p>

Memang di jendela tengah tersebut memberikan banyak sekali paket paket yang berhasil ditangkap oleh wireshark, untuk melihat apakah web yang kiat buka tadi berhasil ditangkap atau tidak, kita bisa lihat di bagian info, jika ada pesan 
''' 200 OK (text/html)'''
maka tandanya wireshark berhasil mendapatkan html kita. 
<br>

### Pertanyaan: Bagaimana kalau 200 OK nya tidak muncul?
Nah ini merupakan masalah umum yang ditemukan, biasanya masalah nya itu disebabkan oleh beberapa hal seperti :
<br>
- *Linknya menggunakan HTTPS, bukan HTTP.* biasanya HTTP akan muncul tanda "not secure" dari web browsernya, jika tidak muncul, mungkin anda bisa ganti link HTTPS nya menjadi HTTP.
- *Masih ada cache.* browser itu mempunyai sebuah cache demi kelancaran dan kecepatan buka website. jika kita baru pertama kali buka link tersebut, maka laptop kita akan request ke server link tersebut untuk meminta HTML nya dan kemudian si-server akan merespon dengan memberikan HTML nya ke web browser kita. nah Informasi tersebut biasanya di simpan di cache(memori sementara) agar ketiak di akses lagi, kita tidak perlu lagi request yang akan membutuhkan waktu lama. Maka dari itu, anda tidak bisa hanay refresh web browser saj (refresh itu hanya memulihkan halaman web nya, tetapi cachenya masih ada), kita perlu meleaukan refresh + hapus cache dengan cara
  1. inspect -> network -> matikan disable cache nya. lalu kita refresh dengan klik *ctrl + Shift + R*
- Cache yang ada di wiresharknya, kita bisa refresh wiresharknya dengan cara:
  <p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week1/asset/CAPTURE.png" alt="Arsitektur Packet Sniffer">
  <br>
</p>

- Tekan Tombol merah (yang di tandai kotak merah diatas), fungsinya untuk memberhentikan atau stop proses pelacakan dan penangkapan paket paket yang ada
- Lalu pilih opsi Capture (yang tandai oleh kotak warna kunimng) untuk mulai penangkapan kembali
- Pilih Wifi (atau ethernet local kalau memakai kabel) dan klik Save.
- Simpan tanpa menyimpan data sebelumnya (jika tidak ingin menambah cache). 

  

## B. Retrieving long document
Sebelumnya kita hanya menggunakan HTMl sederhana yang hanya mengandung 1 -2 kalimat teks saja, untuk kali ini, kita akan mencoba menggunakan HTML dengan teks yang sedikit panjang. 
Langkahnya sama seperti sebelumnya, anda buka wireshark -> wifi dan setelah anda bisa buka link : http://gaia.cs.umass.edu/wireshark-labs/HTTPwireshark-file3.html di browser anda. 
<br>
Setelah itu anda bisa langsung filter dengan mengetikkan "http" lalu cari paket yang terdapat info "200 OK (text/html)".
 <p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week2/aset/Gambar%202.jpeg" alt="Bukti bahwa file besar akan di kirim dlama fragment yang berbeda">
   <br>
</p>
Setelah mendapatkannya, maka klik dan anda akan melihat informasi detail dari paketnya seperti gambar diatas. dalam pengiriman suatu data, untuk HTML yang memiliki elemen yang banyak, HTTP akan mengirimkannya kedalam beberapa fragment hasil pecahan HTML utuh tersebut. untuk HTML dari link diatas, data HTML nya dipecah menjadi 4 Fragmen (yang di gambar disebtu frame). 
<br>

### Pertanyaan: Kenapa harus di pecah? 
alasan simpelnya adalah karena TCP (protokol untuk transport data) itu terbatas, untuk HTML dengan ukuran yang besar, kita tidak bisa mengirimkannay sekaligus, maka dari itu, HTTP akan memecahnya menjadi beberapa fragemen kecil dan kemudian akan dikirim secara sekuensial (karena pakai protokol TCP, jadi data dikiirim dalam urutan untuk menjaga agar data sampai ketujuan dengan selamat). 

Kita juga bisa lihat pemecahannya ketika wireshark menangkap suatu paket:
<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week2/aset/Gambar%203(1).jpeg" alt="Bukti bahwa file besar akan di kirim dlama fragment yang berbeda">
   <br>
</p>
Tanda panah ke kanan (simbol yang berada di palin kiri) menandakan request yang kita lakukan ke server untuk meminta data

<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week2/aset/gambar%204(1).jpeg" alt="Bukti bahwa file besar akan di kirim dlama fragment yang berbeda">
   <br>
</p>
Sedangkan tanda panah ke kiri menandakan hasil response dari server. 
<br>
ditengah antara request dan response tersebut terdapat beberaap TCP yang masuk, beberapa TCP itu adalah data yang dikirim dari server ke web browser kita, dalam paket itu, ada beberapa TCP yang dilacak, itu artinya paket HTML yang besar tersebut dipecah menjadi beberapa paket TCP yang lebih kecil (frame/fragmen) agar bisa di kirim. 

## C. HTML Documents dengan Embedded Objects
Kali ini kita mencoba bagaimana wireshark melacak objek yang di unduh ketika file html atau suatu website mempunyai objek didalamnya (bisa berupa foto, video, icon/gambar, dll). 
<br>
Langkahnya sama, kita tinggal masukkan link browser berikut untuk melakukan pengujiannya :http://gaia.cs.umass.edu/wireshark-labs/HTTPwireshark-file4.html
Jika sudah, anda bisa klik. Pastikan HTML nya punya gambar seperti tampilan HTML dibawah ini:

<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week2/aset/gambar%205.jpeg" alt="Bukti bahwa file besar akan di kirim dlama fragment yang berbeda">
   <br>
</p>

Jika kita lihat pada bagian inspect dengan cara klik kanan -> inspect. kita akan melihat bahwa gambarnya tersebut merupakan gambar dalam bentuk link menggunakan kode html
''' img src ="" ''' dan bukan di simpan dalam file lokal, karena diakses di http juga, maka seharusya jika kita melakukan pelacakan di wireshark (filter HTTP), kiat akan menemukan link http dari ke 2 gambar tersebut

<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week2/aset/gambar%206(1).jpeg" alt="Bukti bahwa file besar akan di kirim dlama fragment yang berbeda">
   <br>
</p>

Bisa dilihat pada gambar terdapat HTTP untuk PNG (icon logo) dan juga jpeg (sampul buku) yang menandakan bahwa wireshark juga dapat melacak suatu http didalam http lain karena keduanya berada di jaringan yang sama. 

## D. HTTP Authentication
Terakhir mari kita coba untuk mengunjungi website yang memiliki pelindung didalamnya (berupa sandi) dan melihat urutan pesan http yang di tangkap oleh wireshark. 
URL-nya: http://gaia.cs.umass.edu/wiresharklabs/protected_pages/HTTP-wireshark-file5.html
<br> 
website tersebut dilindungi oleh kata sandi, maka jika anda ingin mengaksesnya, anda bisa masukkan username dan passwordnya
username: wireshark-students
password: network

Jika sudah klik URL nya, maka tampilannya akan seperti ini:
<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week2/aset/gambar%207.jpeg" alt="Bukti bahwa file besar akan di kirim dlama fragment yang berbeda">
   <br>
</p>
kita masukkan username dan passwordnya, setelah dimasukkan tampilan HTML-nya akan menjadi seperti ini:
<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week2/aset/gambar%208.jpeg" alt="Bukti bahwa file besar akan di kirim dlama fragment yang berbeda">
   <br>
</p>

Sekarang mari kita lihat di bagian wiresharknya, anda bisa menunggu terlebih dahulu lalu filter untuk HTTP. Jika sudah, anda akan melihat gambar seperti dibawah ini
<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week2/aset/gambar%209(1).jpeg" alt="Bukti bahwa file besar akan di kirim dlama fragment yang berbeda">
   <br>
</p>

Pada gambar yang saya tandai, info 401 Unaothorized merupakan web sebelum kita memasuki sandi, setelah kita masuki sandi dan username nya, maka paket berikutnya (dibawah Unauthorized) akan muncul sebagai bukti bahwa kita sudah mendapatkan izin mengunjungi web http tersebut.

<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week2/aset/gambar%209(1).jpeg" alt="Bukti bahwa file besar akan di kirim dlama fragment yang berbeda">
   <br>
</p>

Tetapi karena website ini menggunakan HTTP alih alih HTTPS(tidak ada secure), artinay snadi yang kiat masuki tadi dapat dengan mudah dlihat oleh orang lain. Sandi ini biasanya disimpan dalam bentuk encoder basic authentication. 
<br>
Cara mendapatkan encoder Auth nya adalah, anda tinggal klik paket yang berada di bawah Unauthorized tersebut, masuk ke bagian "Hyper Transfer Protocol", disitu akan ada Authorization dengan encodenya 
'''Basic d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms'''

<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week2/aset/gambar%2010(1).jpeg" alt="Bukti bahwa file besar akan di kirim dlama fragment yang berbeda">
   <br>
</p>

Jika kita mencoba untuk melakukan decoder (mengubah kode Diatas menjadi plain text), kita akan mendapatkan kembali username:password kita

<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week2/aset/gambar%2011.png" alt="Bukti bahwa file besar akan di kirim dlama fragment yang berbeda">
   <br>
</p>

## KESIMPULAN


