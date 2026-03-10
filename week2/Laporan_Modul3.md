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
<br>
3. Buka link : http://gaia.cs.umass.edu/wireshark-labs/HTTPwireshark-file1.html di browser anda.
<br>
5. Tunggu hasilnya di Wireshark, jika sudah muncul protokol HTTP, kita bisa langsung filter dengan cara ketik http di search/pencarian
<br>

(MASUKKAN GAMBAR FILTER HTTP DISINI DAN BERIKAN KE USER HASILNYA)

Memang di jendela tengah tersebut memberikan banyak sekali paket paket yang berhasil ditangkap oleh wireshark, untuk melihat apakah web yang kiat buka tadi berhasil ditangkap atau tidak, kita bisa lihat di bagian info, jika ada pesan 
''' 200 OK (text/html)'''
maka tandanya wireshark berhasil mendapatkan html kita. 
<br>

### Pertanyaan: Bagaimana kalau 200 OK nya tidak muncul?
Nah ini merupakan masalah umum yang ditemukan, biasanya masalah nya itu disebabkan oleh beberapa hal seperti :
<br>
- Linknya menggunakan HTTPS, bukan HTTP, biasanya HTTP akan muncul tanda "not secure" dari web browsernya, jika tidak muncul, mungkin anda bisa ganti link HTTPS nya menjadi HTTP.
- Masih ada cache. browser itu mempunyai sebuah cache demi kelancaran dan kecepatan buka website. jika kita baru pertama kali buka link tersebut, maka laptop kita akan request ke server link tersebut untuk meminta HTML nya dan kemudian si-server akan merespon dengan memberikan HTML nya ke web browser kita. nah Informasi tersebut biasanya di simpan di cache(memori sementara) agar ketiak di akses lagi, kita tidak perlu lagi request yang akan membutuhkan waktu lama. Maka dari itu, anda tidak bisa hanay refresh web browser saj (refresh itu hanya memulihkan halaman web nya, tetapi cachenya masih ada), kita perlu meleaukan refresh + hapus cache dengan cara
  1. inspect -> network -> matikan disable cache nya. lalu kita refresh dengan klik *ctrl + Shift + R*
- Cache yang ada di wiresharknya, kita bisa refresh wiresharknya dengan cara:
  

## B. 
