
## Nama: Niko Rajani Syahputra Pane
## Kelas: IF-04-04
## NIM: 103072400167

# Pertanyaan 

## Pertanyaan NSLOOKUP https://lms.telkomuniversity.ac.id/
Beberapa pertanyaan yang di ajukan adalah:
1. Jalankan nslookup untuk mendapatkan alamat IP dari server web di Asia. Berapa alamat IP server tersebut?
2. Jalankan nslookup agar dapat mengetahui server DNS otoritatif untuk universitas di Eropa.
3. Jalankan nslookup untuk mencari tahu informasi mengenai server email dari Yahoo! Mail melalui salah satu server yang didapatkan di pertanyaan nomor 2. Apa alamat IP-nya?
---

## Jawaban
### 1. Dengan menjalankan ns look up dengan query:
``` python 
nslookup lms.telkomuniversity.ac.id 8.8.8.8
```
Kita mendapatkan hasil:

![Cara Kerja AI](./Assets/nslookupip.png)
dimana alamat addres dari web lms.telkomuniversity.ac.id ada 2, yaitu 

- 104.21.80.193
- 172.67.153.77

alamat IP dua seperti ini sudah jadi hal biasa, karena untuk website yang trafic jaringannaya banyak, kiat perlu beberapa alamat ip yang berbeda, fungsinya agar beban pengujung dibagi rata, dan jika satu server bermasalah, kita bisa akses ip yang lain.

### 2. Jalankan NSLOOKUP agar dapat mengetahui server DNS otoritatif untuk universitas di eropa

Disini kita bisa mencoba query 
``` python
nslookup -type=NS ox.ac.uk 8.8.8.8
```
untuk mendapatkan hasil:

![Cara Kerja AI](./Assets/2.png)

### 3. Jalankan nslookup untuk mencari tahu informasi mengenai server email dari Yahoo! Mail melalui salah satu server yang didapatkan di pertanyaan nomor 2. Apa alamat IP-nya?

### Percobaan 1
Disini kita mencoba kita gunakan dns0.ox.ac.uk dengan IP: 129.67.1.190.

dengan query
``` python 
nslookup -type=MX yahoo.com 129.67.1.190
```
didapat hasilnya:
![Cara Kerja AI](./Assets/3.png)

Hal ini mungkin saja karena server DNS Oxford (129.67.1.190) mungkin diatur hanya untuk menjawab pertanyaan tentang domain mereka sendiri (Oxford) dan menolak kueri luar (Yahoo).

untuk itu kita lanjut ke percobaan ke 2
### Percobaan 2

disini kita akan langsung menggunakan yahoo.com tanpa melalui DNS oxford

dengan query:
```python
nslookup -type=MX yahoo.com
```
hasilnya:
![Cara Kerja AI](./Assets/4.png)

Lalu dari hasil itu, kita coba pakai salah satu alamat IP Server mail nya yaitu:
**mta7.am0.yahoodns.net**

Lalu dengan query:
```python
nslookup mta7.am0.yahoodns.net
```
Hasilnya berupa beberapa alamat IP seperti gambar dibawah ini:

![Cara Kerja AI](./Assets/5.png)
