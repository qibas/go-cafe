## Rajendra Rifqi Baskara - 2306245680

# Link PWS: http://rajendra-rifqi-gocafe.pbp.cs.ui.ac.id


## Pembuatan Project Django
Membuat Folder bernama go-cafe sebagai direktori utama di file explorer lokal saya, setelah itu membuat file txt bernama requirements.txt yang 
berisi dependencies yang ada di tutorial 0. Buat Virtual Environment di command prompt dengan direktori yang sudah dibuat diawal tadi lalu aktifkan env yang berguna agar tidak bertabrakan dengan versi lain, lalu setleah diaktifkan install requirments.txt di command prompt berupa 

```pip install -r requirements.txt```


Setelah menginstall requirments.txt , kita buat project django yang kita inginkan, yaitu go_cafe dengan perintah 
```django-admin startproject go_cafe .``` 
di command prompt dengan env yang masih akfitf, yang dimana nanti akan muncul direktori baru berupa project yang kita buat. Setelah itu, kita tambahkan ```settings.py``` di direktori go_cafe dengan "localhost", "127.0.0.1" di ALLOWED_HOSTS. Lalu, kita jalankan server project django kita dengan perintah python ```manage.py``` runserver dan buka ```http://localhost:8000``` untuk melihat apakah rocket sudah muncul atau belum.Lalu, tambahkan berkas .gitignore di direktori utama, sebelum ditambahkan nonaktifkan env terlebih dahulu. Lakukan git add dan commit serta git push ke github.

## Menambahkan 'main' di INSTALLED_APPS
Setlah melakukan semua itu, buat aplikasi main dalam proyek go-cafe dengan memerintahkan python manage.py startapp main, sehingga akan ditambahkan folder baru di direktori utama proyek go-cafe. Di dalam go cafe terdapat settings.py untuk mendaftarkan main ke dalam proyek go-cafe, dengam menambahkan 'main' di INSTALLED_APPS.

## Route URL pada aplikasi 'main'
Membuat routing pada urls.py agar aplikasi main dapat diakses melalui peramban web. Urls.py dilakukan dengan membuat file di direktori main. Urls.py berisi app_name = 'main' urlpatterns = [ path('', show_main, name='main_urls'), ] yang dimana isi tersebut untuk mengatur rute URL yang terkait dengan aplikasi main.


aplikasi main yang dimaksud, yaitu file main.html yang dimana untuk menampilkan proyek Django pada direktori proyek saya.Lalu pada berkas models.py saya menambahkan atribut-atribut yang saya definisikan adalah name,price,description yang diwajibkan.Setelah saya membuat atribut pada models.py, saya membuat dictionary yang berisikan value, hal itu dari views.py di direktori main juga.

views.py terdapat return render yang dimana berfungsi untuk mengantar isi dari dictionary content ke template HTML yang sudah saya buat, berikut tampilan server HTML saya:

### GO CAFE
Name Product:
{{ name }}

Price:
{{ price }}

Description:
{{ description }}

## Deploy PWS
Untuk melakukan upload pada PWS, saya membuka halaman PWS link khusus PWS dan melakukan login. Pertama-tama saya buat new project pada PWS dan menamai proyeknya dengan gocafe.

Untuk menjalankan aplikasi Django di pws dan local, kita perlu mengatur variabel ALLOWED_HOSTS di file ```settings.py```

```ALLOWED_HOSTS = ["localhost", "127.0.0.1","rajendra-rifqi-gocafe.pbp.cs.ui.ac.id"]```

## Penjelasan request client ke web aplikasi berbasis Django![Flowchart (1)](https://github.com/user-attachments/assets/aae9d899-e6a5-4541-9cc0-fffe9cb69400)


    **HTTP Request** berfungsi untuk melakukan permintaan yang dikirimkan dari klien ke server.

    **urls.py** bertanggung jawab untuk memetakan URL yang diminta oleh klien ke fungsi atau view yang sesuai di dalam aplikasi

    **views.py** berisi logika pemrosesan permintaan. View akan mengakses model untuk mendapatkan data dari database (jika diperlukan), atau langsung merender template dan mengirimkan respons HTML ke klien. Fungsi views.py mengembalikan objek HTTP Response berupa HTML

    **models.py** berisi definisi model-model yang berhubungan dengan database. Misal, jika views.py membutuhkan daftar pengguna, ia akan meminta data tersebut melalui model yang terdefinisi di models.py

    **Template(main.html):** Setelah view selesai memproses data, biasanya view akan merender template untuk mengahsilkan halaman HTML. Template ini diisikan dengan variabel yang akan diisi dengan *data dari view*.

## Fungsi Git dalam Perangkat Lunak
Git adalah sistem kontrol versi terdistribusi yang digunakan untuk melacak perubahan dalam kode atau berkas dalam proyek perangkat lunak. Dalam pengembangan perangkat lunak sangat penting untuk bekerja pada proyek yang sama secara bersamaan.

Dengan Git, setiap salinan lokal dari repositori adalah backup lengkap dari sejarah perubahan proyek. Ini memungkinkan pengembang untuk memulihkan proyek ke versi tertentu jika terjadi kesalahan.

## Mengapa Django sangat penting untuk Pemula dalam pengembangan perangkat lunak?
Django adalah salah satu pengembangan web yang populer. **Mengapa demikian?**
Karena dapat menyederhanakan proses pembuatan aplikasi web yang kompleks. Ada beberapa alasan mengapa Django sangat penting dan berguna, yaitu:
1. **Build Arsitekturnya tersusun rapih**:
    Django mengikuti pola arsitektur Model-View-Template (MVT) yang membantu pemula memahami bagaimana memisahkan logika aplikasi (Models), tampilan pengguna (Templates), dan pengendalian logika aplikasi (Views).
2. **Integrasi dengan berbagai app**:
    Dengan Django, kita dapat menggunakan "apps" — komponen yang dapat digunakan kembali — yang memungkinkan kita membangun proyek dengan menggabungkan beberapa app.

Alasan inilah mengapa kita belajar dengan MVT sebagai bahan dasar, karena mudah dipahami bagi pemula.

## Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut ORM (Object-Relational Mapping) karena Django memungkinkan pengguna untuk berinteraksi dengan basis data menggunakan kode Python. Dalam Django, model adalah representasi dari tabel di Database. Setiap model yang kita buat di Django, secara otomatis akan dipetakan ke tabel database.

Alasan diantaranya, karena:

1. **Objek Python**: Django mengizinkan pengembang untuk berinteraksi dengan database menggunakan objek Python, tanpa harus menulis query SQL.
2. **Mapping Otomatis**: Django secara otomatis memetakan atribut model ke kolom di tabel database. Jadi, jika kita membuat model dengan atribut seperti name, price, atau description, Django akan membuat kolom dengan nama-nama tersebut di tabel database. Dalam kata lain, models adalah sebuah schema untuk database.