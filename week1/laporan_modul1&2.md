# Laporan Praktikum Jaringan Komputer
**Nama:** Niko Rajani Syahputra
**NIM:** 103072400167
**Modul:** 1 & 2 (Instalasi & Pengenalan Tools Wireshark)

## 1. Pendahuluan
Pemahaman mendalam mengenai protokol jaringan tidak cukup hanya dengan teori, melainkan harus dibuktikan dengan pengamatan langsung terhadap paket data yang mengalir di dalam jaringan. Melalui praktikum ini, kita menggunakan **Wireshark**, sebuah perangkat lunak *packet sniffer* yang memungkinkan kita untuk menangkap ("sniff") dan menganalisis pesan yang dipertukarkan antara entitas protokol secara pasif.

Tujuan utama dari praktikum ini adalah untuk memastikan kesiapan perangkat lunak pendukung dan memahami komponen utama antarmuka Wireshark guna mengidentifikasi paket data dalam skenario jaringan nyata.


## 2. Modul 1: Persiapan Lingkungan (Running Modul)
Pada tahap awal, dilakukan verifikasi dan instalasi *tools* dasar yang akan digunakan selama satu semester ke depan.

### Perangkat Lunak yang Digunakan:
* **Wireshark:** Digunakan sebagai penganalisis protokol jaringan utama.
* **Python 3:** Digunakan untuk mendukung modul pemrograman *socket* di pertemuan mendatang.


## 3. Modul 2: Pengenalan Tools Wireshark
Modul ini berfokus pada cara kerja *Packet Sniffer* dan pengenalan antarmuka grafis (GUI) Wireshark.

### 3.1 Struktur Packet Sniffer
Wireshark bekerja dengan bantuan *Packet Capture Library* yang menerima salinan setiap *frame* lapisan link (*link layer*) yang dikirim atau diterima oleh komputer, baik melalui Ethernet maupun WiFi.

<p align="center">
  <img src="path/ke/gambar-arsitektur.png" alt="Arsitektur Packet Sniffer">
  <br>
  <em>Gambar 3.1: Struktur dasar sebuah Packet Sniffer</em>
</p>

### 3.2 Antarmuka Utama Wireshark
Berdasarkan pengamatan pada aplikasi, terdapat lima komponen utama yang harus dipahami:
* **Command Menus:** Menu standar (File, Edit, Capture, dll.) untuk mengelola aktivitas aplikasi.
* **Packet-Listing Window:** Menampilkan ringkasan satu baris untuk setiap paket yang tertangkap, termasuk nomor, waktu, sumber, tujuan, dan jenis protokol.
* **Packet-Header Details Window:** Memberikan rincian protokol dari paket yang dipilih, memberikan rincian tentang frame Ethernet dan datagram IP.
* **Packet-Contents Window:** Menampilkan seluruh isi frame yang diambil dalam format ASCII dan heksadesimal.
* **Filter Display Field:** Tempat memasukkan nama protokol (seperti "http") untuk menyaring informasi yang ditampilkan di jendela daftar paket.


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
