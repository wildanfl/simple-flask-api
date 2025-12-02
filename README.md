# Flask

Projek ini adalah contoh implementasi sederhana untuk membuat web server CRUD menggunakan Flask dan MySQL Workbench.

## Persyaratan
Sebelum memulai, pastikan Anda sudah memenuhi persyaratan berikut:
* Python 3.x
* Flask framework (pip install flask)
* MySQL Workbench (atau server MySQL lainnya)
* mysql-connector-python (pip install mysql-connector-python)

## Instalasi
1.  Clone repositori ini ke dalam direktori lokal Anda
2.  Buat database baru pada MySQL Workbench dengan nama `db_nilai` dan tabel `mahasiswa`. Tabel mahasiswa memiliki kolom-kolom berikut:
    - NIM (varchar(50))
    - Nama (varchar(255))
    - Kelas (varchar(50))
    - Fundamental_Cloud (int)
    - Db (int)
    - Py (int)
    - Linux (int)
    
3.  Sesuaikan koneksi ke database pada file app.py dengan informasi login dan host yang sesuai dengan konfigurasi MySQL Workbench Anda.
4.  Jalankan file app.py pada terminal dengan perintah python app.py.
5.  Buka browser dan akses alamat http://localhost:5000.
