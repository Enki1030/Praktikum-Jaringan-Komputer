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
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week1/carakerjasniffset.png" alt="Arsitektur Packet Sniffer">
  <br>
  <em>Gambar 3.1: Struktur dasar sebuah Packet Sniffer</em>
</p>

Wireshark bekerja dengan bantuan *Packet Capture Library* yang menerima salinan setiap *frame* lapisan link (*link layer*) yang dikirim atau diterima oleh komputer, baik melalui Ethernet maupun WiFi.

<p align="center">
  <img src="https://github.com/Enki1030/Praktikum-Jaringan-Komputer/blob/main/week1/carakerjasniffset.png" alt="Arsitektur Packet Sniffer">
  <br>
  <em>Gambar 3.1: Struktur dasar sebuah Packet Sniffer</em>
</p>

Frame ini ibarat sebuah informasi unik yang dikirimkan oleh komputer sebagai identitas dari suatu device, seperti IP, Protocol, Dll.

## 4. Analisis Pengenalan Protokol HTTP
Sesuai instruksi modul, dilakukan pengujian dengan mengakses URL untuk memicu lalu lintas HTTP dan mengamati interaksi protokol secara langsung.

### Langkah Identifikasi HTTP:
1.  **Filtering:** Mengetik "http" pada kolom filter untuk mengisolasi paket dari protokol lain agar hanya pesan HTTP yang ditampilkan.
2.  **Selection:** Memilih paket dengan metode **GET** yang dikirim dari komputer klien ke server tujuan.
3.  **Inspection:** Memperluas bagian *Hypertext Transfer Protocol* pada jendela detail untuk melihat konten terperinci seperti pesan aplikasi yang ditemukan dalam segmen TCP.

<p align="center">
  <img src="path/ke/gambar-http-result.png" alt="Hasil Capture HTTP">
  <br>
  <em>Gambar 4.1: Detail pesan HTTP GET yang berhasil ditangkap</em>
</p>

> **Catatan Penting:** Sebuah *Packet Sniffer* itu sendiri bersifat pasif. Ia hanya menerima salinan paket yang dikirim/diterima oleh aplikasi dan tidak pernah mengirim ataupun menerima paket itu sendiri secara aktif.


## 5. Kesimpulan
Instalasi Wireshark dan Python telah berhasil dilakukan dan dipastikan berfungsi dengan baik. Melalui pengenalan tools ini, praktikan kini dapat memahami struktur antarmuka Wireshark dan mampu melakukan pemfilteran protokol dasar (HTTP) untuk menganalisis pesan yang lewat di dalam jaringan. Pengetahuan ini menjadi fondasi utama untuk praktikum eksplorasi protokol yang lebih kompleks pada modul berikutnya.
