# Laporan Praktikum Jaringan Komputer
**Nama:** Niko Rajani Syahputra
**NIM:** 103072400167
**Modul:** 1 & 2 (Instalasi & Pengenalan Tools Wireshark)

## 1. Pendahuluan
Praktikum Jaringan Komputer ini memberikan pembelajaran dan praktik dari matakuliah jaringan komputer teori. Melalui praktikum ini, kita menggunakan **Wireshark**, sebuah perangkat lunak *packet sniffer* yang memungkinkan kita untuk mengambil  ("sniff") dan menganalisis pesan yang bertukar antar protokol yang bisa di lihat di wireshark. 

## 2. Modul 1: Persiapan Lingkungan (Running Modul)
Pada tahap awal ini, kita akan menginstall sebuah perangkat yang aka di gunakan selama satu semester. 

### Perangkat Lunak yang Digunakan:
* **Wireshark:** Digunakan sebagai penganalisis protokol jaringan utama.
  Jika belum terinstall dapat di download pada link berikut http://www.wireshark.org/
  
* **Python 3:** Digunakan untuk mendukung modul pemrograman *socket* di pertemuan mendatang.
  Jika belum terinstall dapat di download pada link berikut https://www.python.org/downloads/


## 3. Modul 2: Pengenalan Tools Wireshark
Modul ini berfokus pada cara kerja *Packet Sniffer* dan pengenalan antarmuka grafis (GUI) Wireshark. Di sini kita akan mulai untuk mencoba mengulik software ini, mulai dari tool yang ada, cara kerjanya dan bagaimana wireshark ini berguna untuk tugas analisis jaringan. 
<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week1/carakerjasniffset.png" alt="Arsitektur Packet Sniffer">
  <br>
  <em>Gambar 3.1: Struktur dasar sebuah Packet Sniffer</em>
</p>

Seperti yang terlihat di gambar atas, gambar tersebut adalah tampilan awal dari wireshark, jika kita lihat di bagian yang berwarna merah, dapat terlihat beberapa jenis jaringan mulai dari WIFI (wireless) dan Wire (Local Area Connection) dan beberapa network lainnya seperti virtual network(Host virtual Network). 


Jika kita klik salah satu (Karena saya terhubung dengan wifi makanya bisa di track dan di analisis), maka tampilannya akan menjadi seperti ini:

<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week1/asset/tampilan%20wifi.png">
  <br>
  <em>Gambar 3.1: Struktur dasar sebuah Packet Sniffer</em>
</p>

Wireshark bekerja dengan bantuan *Packet Capture Library* yang menerima salinan setiap *frame* lapisan link (*link layer*) yang dikirim atau diterima oleh komputer, baik melalui Ethernet maupun WiFi.

<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week1/carakerjasniffset.png" alt="Arsitektur Packet Sniffer">
  <br>
  <em>Gambar 3.1: Struktur dasar sebuah Packet Sniffer</em>
</p>

1. Kotak merah = berisi informasi paket-paket yang berhasil ditangkap dalam satu baris untuk setiap paket seperti protokol, destination, time dll. 
Frame ini ibarat Sebuah informasi unik yang dikirimkan oleh komputer sebagai identitas dari suatu device, seperti IP, Protocol, Dll.

2. Kotak Kuning = Berisi detail teknis dari suatu paket yang ada yaitu ada frame(informasi dari satu paketnya), serta protokol yang dia gunakan (TCP/UDP).

3. Kotak Biru = Berisi detail dari frame yang di petakan kedalam sebuah heksadesimal.

ke 3 tampilan diatas lah yang akan kita gunakan untuk melakukan analsis secara mendalam. selanjtunya kita akan mencoba untuk menganalisis bagaimana Wireshark dapat mengenali protokol seperti HTTP

## 4. Analisis Pengenalan Protokol HTTP
Kita akan menggunakan contoh sederhana untuk HTTP, Link nya bisa anda akses dibawah ini:
http://gaia.cs.umass.edu/wiresharklabs/INTRO-wireshark-file1.html

tugas kita sederhana, yaitu memastikan dan melihat bagaimana cara kerja wireshark dalam menerima paket paket dari jaringan. 

Langkah Langkah nya

- Buka Link diatas (bisa di chrome atau edge atau search engine sejenis)
- Masuk klik pada bagian Wifi (atau ethernet local yang menampilkan grafik kalau anda menggunakan wire/kabel)
- Nanti akan muncul tampilan seperti gambar seperti dii bawah ini:
<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week1/carakerjasniffset.png" alt="Arsitektur Packet Sniffer">
  <br>
  <em>Gambar 3.1: Struktur dasar sebuah Packet Sniffer</em>
</p>
kita cukup perhatikan kotak warna merah dan fokus ke protokol, apakah ada protokol yang bernama HTTP
jika tidak ada, maka anda bisa melakukan restart dengan cara:

<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week1/carakerjasniffset.png" alt="Arsitektur Packet Sniffer">
  <br>
  <em>Gambar 3.1: Struktur dasar sebuah Packet Sniffer</em>
</p>

a. Tekan Tombol merah seperti yang di tandai warna biru untuk memberhentikan atau stop proses pelacakan dan penangkapan paket paket yang ada
b. Lalu pilih opsi Capture (yang tandai oleh kotak warna merah) untuk mulai penangkapan kembali
c. Pilih Wifi (atau ethernet local kalau memakai kabel) dan klik Save.
d. Simpan tanpa menyimpan data sebelumnya (jika tidak ingin menambah cache). 


Jika masih belum muncul, anda bisa restart Chrome/edge beberapa kali atau berpindah ke search engine yang lain. 
Jika sudah ketemu (biasanya akan muncul beberapa paket), anda bisa melakukan filter dengan cara pergi ke bagian search(dibagian atas) lalu ketik "http" untuk mealkukan filter hanya pada protokol HTTP. 

Jika sudah, maka tampilannya seperti ini:
<p align="center">
  <img src="path/ke/gambar-http-result.png" alt="Hasil Capture HTTP">
  <br>
  <em>Gambar 4.1: Detail pesan HTTP GET yang berhasil ditangkap</em>
</p>

Anda bisa Pilih Info 2"00 OK (Text/HTML)" dan kemudian masuk kebagian Kiri bawah untuk detail dari paketnya. 

<p align="center">
  <img src="path/ke/gambar-http-result.png" alt="Hasil Capture HTTP">
  <br>
  <em>Gambar 4.1: Detail pesan HTTP GET yang berhasil ditangkap</em>
</p>

Disitu akan ada "Line Based text data", klik untuk membuak informasi detailnya. 
Jika terdapat struktur HTML seperti:
"Congratulations! You've downloaded the first Wireshark lab file!" (seperti yang muncul pada tulisan HTML di browser anda), maka selamat, kiat telah berhasil menamatka wireshark!!. 

> **Catatan Penting:** Sebuah *Packet Sniffer* itu sendiri bersifat pasif. Ia hanya menerima salinan paket yang dikirim/diterima oleh aplikasi dan tidak pernah mengirim ataupun menerima paket itu sendiri secara aktif.


## 5. Kesimpulan
Instalasi Wireshark dan Python telah berhasil dilakukan dan dipastikan berfungsi dengan baik. Melalui pengenalan tools ini, praktikan kini dapat memahami struktur antarmuka Wireshark dan mampu melakukan pemfilteran protokol dasar (HTTP) untuk menganalisis pesan yang lewat di dalam jaringan. Pengetahuan ini menjadi fondasi utama untuk praktikum eksplorasi protokol yang lebih kompleks pada modul berikutnya.
