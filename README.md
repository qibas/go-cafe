# Profil 
- Rajendra Rifqi Baskara - 2306245680
- Kelas: PBP C
#

# Link PWS: http://rajendra-rifqi-gocafe.pbp.cs.ui.ac.id

# Content
- [TUGAS 2](#tugas-2)
- [TUGAS 3](#tugas-3)
- [TUGAS 4](#tugas-4)
#

# Tugas 2 
[Back to Contents](#contents)

## Pembuatan Project Django
Membuat Folder bernama go-cafe sebagai direktori utama di file explorer lokal saya, setelah itu membuat file txt bernama requirements.txt yang 
berisi dependencies yang ada di tutorial 0. Buat Virtual Environment di command prompt dengan direktori yang sudah dibuat diawal tadi lalu aktifkan env yang berguna agar tidak bertabrakan dengan versi lain, lalu setleah diaktifkan install requirments.txt di command prompt berupa 

```bash
pip install -r requirements.txt
```


Setelah menginstall requirments.txt , kita buat project django yang kita inginkan, yaitu go_cafe dengan perintah
``` bash
django-admin startproject go_cafe .
``` 
di command prompt dengan env yang masih akfif, yang dimana nanti akan muncul direktori baru berupa project yang kita buat. Setelah itu, kita tambahkan ```settings.py``` di direktori go_cafe dengan "localhost", "127.0.0.1" di ALLOWED_HOSTS. Lalu, kita jalankan server project django kita dengan perintah python ```manage.py``` runserver dan buka ```http://localhost:8000``` untuk melihat apakah rocket sudah muncul atau belum.Lalu, tambahkan berkas .gitignore di direktori utama, sebelum ditambahkan nonaktifkan env terlebih dahulu. Lakukan git add dan commit serta git push ke github.

## Menambahkan 'main' di INSTALLED_APPS
- Setelah melakukan semua itu, buat aplikasi main dalam proyek go-cafe dengan memerintahkan python manage.py startapp main, sehingga akan ditambahkan folder baru di direktori utama proyek go-cafe. Di dalam go cafe terdapat settings.py untuk mendaftarkan main ke dalam proyek go-cafe, dengam menambahkan 'main' di INSTALLED_APPS.
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
]
```

## Route URL pada aplikasi 'main'

- Menambahkan class Product di `models.py` dengan attribute name,price,description.
```bash
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
```
lakukan migrasi di terminal dengan command berikut:
```bash
python manage.py makemigrations
python manage.py migrate
```

- Aplikasi main yang dimaksud, yaitu file main.html yang dimana untuk menampilkan proyek Django pada direktori proyek saya.

- Membuat fungsi di ``views.py`` untuk dihubungkan dengan ``main.html``:
```bash
from django.shortcuts import render,redirect

# Create your views here.
def show_main(request):
    context = {
        'name': 'American Express',
        'price': 'Rp28.000',
        'description': 'A strong black coffee drink made from espresso and hot water. Americano has a strong taste, but is not too bitter because it is mixed with water.',
        'name_person' : 'Rajendra Rifqi Baskara',
        'class_name': 'PBP C',
        'npm' : '2306245680',
    }

    return render(request, "main.html", context)
```
- Membuat routing pada `urls.py` agar aplikasi main dapat diakses melalui peramban web. Urls.py dilakukan dengan membuat file di direktori main.  yang dimana isi tersebut untuk mengatur rute URL yang terkait dengan aplikasi main.
```bash
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
kemudian tambahkan rute URL baru untuk mengarahkan tampilan `main` di dalam variable urlpatterns.
```bash
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
```

## Deploy PWS
Untuk melakukan upload pada PWS, saya membuka halaman PWS link khusus PWS dan melakukan login. Pertama-tama saya buat new project pada PWS dan menamai proyeknya dengan gocafe.

Untuk menjalankan aplikasi Django di pws dan local, kita perlu mengatur variabel ALLOWED_HOSTS di file ```settings.py```

```bash
ALLOWED_HOSTS = ["localhost", "127.0.0.1","rajendra-rifqi-gocafe.pbp.cs.ui.ac.id"]
```

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

# Tugas 3
[Back to Contents](#contents)

## Data delivery sangat penting dalam implementasi platform? Mengapa demikian??

Data delivery melakukan transfer data antara klien (misal, browser dari pengguna atau aplikasi) dan server. 

Tanpa mekanisme pengiriman data yang efisien menggunakan HTTP, HTTPS, JSON, dan XML, sebuah platform tidak dapat dijalankan dengan baik.

## Lebih baik XML atau JSON? Mengapa JSON lebih populer dibandingkan XML?

Sebenarnya tergantung yang dibutuhkan dalam mengelola data, misal:

- JSON lebih cepat untuk memproses banyak Parsing (memecah data menjadi elemen yang lebih kecil)

- XML Cocok untuk pengembilan data kecil, misal hanya diperlukan mengambil satu atau beberapa elemen dari file XML dalam melakukan parsing.

Pada umumnya memang JSON lebih banyak diminati karena sintaks yang sederhana dalam hal mengimplementasikan teknologi sekarang

referensi: https://stackoverflow.com/questions/26115338/which-is-the-better-performance-to-read-values-from-xml-or-json

## Fungsi ``is_valid()`` pada form Django dan mengapa membutuhkan tersebut?

fungsi ``is_valid()`` adalah suatu validasi sebuah data dari input yang berasal dari form. Fungsi ini memberikan pengecekan berupa data yang dikirim ke form, seperti tipe data, dst.

## Mengapa ```csrf_token``` sangat penting? Dan akibat yang ditimbulkan jika tidak memasangnya

```csrf_token``` sangat penting untuk pelindungan web dari serangan CSRF. Cross-Site Request Forgery atau CSRF adalah jenis serangan keamanan yang mencoba memanfaatkan pengguna untuk mengirim permintaan yang tidak diinginkan ke aplikasi web.

## Pemanfaatan CSRF bagi penyerang
Sehingga, dengan CSRF penyerang dapat menjalankan tindakan yang illegal dengan mengubah pengaturan akun pengguna, transfer uang, dan mengirim data tanpa izin. 

referensi: https://docs.djangoproject.com/en/5.1/ref/csrf/

## Step-by-step implementasi checklist

- Step pertama yang dilakukan adalah membuat ``base.html`` pada root project di direktori templates yang baru (beda dengan templates yang berada di `main`)
```bash
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

- kemudian, saya menambah mengisi berikut pada ``settings.py`` di direktori proyek ``go_cafe`` 
```bash
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    }
]
```
perintah diatas untuk me-set lokasi template yang digunakan pada proyek go-cafe


- Tambahkan field baru yaitu id sebagai keamanan pada `/main/models.py`
```bash
from django.db import models
import uuid
# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=300)

```
Lakukan migrasi setelah memodifikasi model
- Buat file `forms.py ` di direktori `main` untuk menerima data dari product baru.
```bash
from django.forms import ModelForm
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
```

- Saya kemudian memodifikasi `views.py` dengan menambahkan method `create_product` untuk membuat form dalam penambahan produk ketika di submit atau di add dari form

```bash
from django.shortcuts import render,redirect
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product_entry = Product.objects.all()
    context = {
        'name': 'American Express',
        'price': 'Rp28.000',
        'description': 'A strong black coffee drink made from espresso and hot water. Americano has a strong taste, but is not too bitter because it is mixed with water.',
        'name_person' : 'Rajendra Rifqi Baskara',
        'class_name': 'PBP C',
        'npm' : '2306245680',
        'product_entries' : product_entry,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```
- Menambahakn line baru di ```urls.py``` untuk mengimport fungsi `create_product` yang ada di `views.py` dengan path URL agar bisa diakses
```bash
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    ...
]
```
- Mengimplementasikan form yang baru saja dibuat ke dalam berkas laman baru bernama `/templates/create_product.html` dengan menggunakan `base.html`. Berikut kodenya :
```bash
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}

```

- Modifikasi `main/templates/main.html` yang sudah dibuat ditugas sebelumnya untuk menampilkan setiap data products. Saya menambahkan strukturtabel yang lebih simple dari tugas sebelumnya agar lebih mudah dibaca dan lebih rapih dengan border.
```bash
{% extends 'base.html' %}
{% block content %}
<div style="text-align:center;">
    <h1>GO CAFE</h1>
    <p>Project by 🍵: {{ name_person }} - {{ npm }} - {{ class_name }}</p>
    
    {% if not product_entries %}
    <p>Belum ada data produk pada GoCafe.</p>
    {% else %}
    <table style="width: 100%; margin-top: 20px; border-collapse: collapse;">
        <thead>
            <tr>
                <th style="border: 2px solid #ce5509; padding: 8px;">Coffee Name</th>
                <th style="border: 2px solid #ce5509; padding: 8px;">Price</th>
                <th style="border: 2px solid #ce5509; padding: 8px;">Description</th>
            </tr>
        </thead>
        <tbody>
            {% for product_entry in product_entries %}
            <tr>
                <td style="border: 2px solid #ce5509; padding: 8px;">{{ product_entry.name }}</td>
                <td style="border: 2px solid #ce5509; padding: 8px;">{{ product_entry.price }}</td>
                <td style="border: 2px solid #ce5509; padding: 8px;">{{ product_entry.description }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    {% endif %}
    
    <br />
    <a href="{% url 'main:create_product' %}">
        <button style="padding: 10px 20px; font-size: 16px;">Add Product</button>
    </a>
</div>
{% endblock content %}

```

- Modifikasi `views.py` untuk menampilkan data dalam format XML dan JSON, serta menampilkan data produk sesuai id.
```bash
....
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- Setelah memodifikasi diatas, kita harus menambahkan path baru di `urls.py` agar bisa diakses di URL webnya.
```bash
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_json_by_id, show_xml_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
## Screenshot Postman
**tampilan xml**
![image](https://github.com/user-attachments/assets/2c021153-3822-41d8-863b-dd7e0eb4d32e)

**tampilan json**
![image](https://github.com/user-attachments/assets/fc0960af-ae84-4f43-8bb3-25d45d2d02b2)

**tampilan xml_by_id**
![image](https://github.com/user-attachments/assets/2ea7a801-5554-4660-b0e6-2991a32b3361)

**tampilan json_by_id**
![image](https://github.com/user-attachments/assets/3fa5ba84-a40a-45ef-ad4a-2faea0e1cc42)


# Tugas 4
[Back to Contents](#contents)

## Perbedaan antara `HttpResponseRedirect()` dan `redirect()`

`Redirect()`: redirect ini berguna untuk menampilkan halaman setelah akun berhasil dibuat dari metode permintaan POST.
```bash
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
Dalam fungsi redirect akan segera menampilakn ke halaman `main:;login`

`HttpResponseRedirect()`: metode ini sebenernya mirip fungsinya dengan `redirect()`, tetapi metode ini menggunakan sintaks yang lebih manual.
```bash
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```

Memerlukan reverse() untuk mengubah URL pattern name menjadi URL sebenernya, sehingga sintaks lebih panjang.

## Cara kerja penghubungan model Product dengan User
Pada model `Product`, ada field user yang didefinisikan sebagai `ForeignKey` yang mengarah ke model `User` 
```bash
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

ForeignKey ini menunjukkan bahwa setiap produk (Product) terkait dengan satu pengguna (User), tetapi satu pengguna bisa memiliki banyak produk. Inilah yang disebut dengan relasi `one-to-many.`

Dalam fungsi `show_main`, setiap pengguna yang login akan mendapatkan produk yang dibuat dengan menggunakan filter dibawah ini
```bash
Product.objects.filter(user=request.user)
```
`request.user` mengacu pada objek User yang saat ini login. Dengan demikian, filter(user=request.user) akan mencari semua produk yang dimiliki oleh pengguna yang login.

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Dalam keamanaan web, kedua tahap tersebut sangat dierplukan dalam penegembangan web.
`Authentication`: adalah untuk melakukan autentikasi dan login kepada user yang sudah membuat akun. Fungsi ini memastikan validasi jika pengguna melakukan verifikasinya sudah benar saat masuk kedalam server.

`Authorization`: adalah untuk mengontrol akses apa saja yang bisa dilakukan oleh user saat memasuki server setelah berhasil di diautentikasi. Jadi fungsi ini bisa menentukan user dalam pengaksesan web.

Proses Saat Pengguna Login:
**1. Pengguna Mengisi Form Login:**
- Pengguna mengisi form login dengan username dan password.
- Form login dikirimkan ke server melalui permintaan POST.

**2. Proses Authentication:**

- AuthenticationForm digunakan untuk memvalidasi kredensial yang dimasukkan oleh pengguna.
- Jika form valid (form.is_valid()), maka sistem mengekstrak pengguna (user = form.get_user()) dan memverifikasi kredensial tersebut.
- Jika kredensial cocok dengan yang ada di database, pengguna dianggap terotentikasi.
```bash
def login_user(request):
...
if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
...
```
**3. Proses Login:**
- Fungsi `login(request,user)` diatas digunakan untuk membuat sesi autentikasi bagi pengguna. Django menyimpan informasi pengguna di sesi dan mengatur cookie untuk melacak sesi pengguna tersebut.
```bash
login(request, user)
```

**4. Mengatur Cookie atau Metadata:**
Setelah login, kamu dapat mengatur cookie seperti last_login untuk melacak kapan pengguna terakhir kali login, menggunakan:
```bash
response.set_cookie('last_login', str(datetime.datetime.now()))
```

**Implementasi kedua tahap tersebut:**
`Authentication`:
- Django menggunakan sistem autentikasi bawaan yang mudah digunakan, di mana authenticate() memverifikasi kredensial pengguna terhadap database.
- Fungsi login() membuat sesi pengguna terotentikasi, memungkinkan pengguna untuk mengakses aplikasi sebagai pengguna yang valid.

`Authorization`:
- Django menyediakan mekanisme otorisasi yang terintegrasi, seperti `@login_required` untuk membatasi akses hanya kepada pengguna yang sudah login.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

1. Awalnya pengguna disuruh mengisi form login dan mengirimkan ke permintaan POST.
2. Jika kredensialnya benar, maka `login(request,user)` membuat sesi dan menetapkan cookie sesi *(sessionid)*.
3. Django mengingat pengguna yang login dengan *(sessionid)* ini ke browser pengguna sebagai bagian dari response HTTP setelah login dan memuatnya pada setiap permintaan berikutnya. Jika ID sesi valid, Django akan mengenali pengguna.
4. Pengguna dapat diakses melalui `request.user`, seperti produk yang dimiliki pengguna tersebut

*Cookies memiliki kegunaan lain*:
1. Menyimpan item yang dtitambahkan pengguna, seperti mengelola keranjang belanja di E-Commerce
2. Menjadi pengingat atau notifikasi 
3. Melacak atau Tracking aktifitas pengguna, seperti waktu yang dikunjungi dll.

## Step-by-step Checklist

pertama-tama kita mengimport bawaan dari djagno untuk mengisi formulir pendaftaran saat register akun di direktori `views.py`,
```bash
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
lalu tambahkan fungsi register,
```bash
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
lalu kita buat berkas register.html di direktori `main/templates/`
```bash
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

Tag `{{ form.as_table }} `untuk memudahkan membuat form yang berbentuk tabel agar format lebih jelas.

Lalu kita atur path url ke dalam urlpatterns di direktori `urls.py` untuk mengakses fungsi register ke peramban web.
```bash
path('register/', register, name='register'),
```

Setelah itu kita buat fungsi login_user di `views.py`
```bash
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

Setelah itu, buat tampilan di direktori `main/templates` dengan file `login.html `
```bash
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

lalu kita set kembali path url ke dalam urlpatterns di direktori `urls.py`

Setelah kita membuat akun, kita buat fungsi logout dengan mengimport bawaan dari django di direktori `views.py`
```bash
from django.contrib.auth import logout
```

lalu buat fungsi logoutnya
```bash
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

lalu tambahkan button logout di bawah create product di direktori `main/templates/main.html/`
```bash
<br />
    <a href="{% url 'main:create_product' %}">
        <button style="padding: 10px 20px; font-size: 16px;">Add Product</button>
    </a>

    <a href="{% url 'main:logout' %}">
        <button style="padding: 10px 20px; font-size: 16px; margin-top: 10px;">Logout</button>
        <h5>Sesi terakhir login: {{ last_login }}</h5>
    </a>
```

`{% url 'main:logout' %}` digunakan untuk mengarah ke URL secara dinamis berdasarkan app_name dan name yang sudah didefinisikan di `urls.py`

Kita inisiasikan path url logout di `urls.py `
```bash
from main.views import logout_user
...

urlpatterns = [
    ...
    path('logout/', logout_user, name='logout') 
    ...
]
```

## SS Akun dengan dummy masing-masing

**Akun: Qibas**
<img width="1324" alt="Screenshot 2024-09-22 at 12 40 21" src="https://github.com/user-attachments/assets/e5b1f7d6-5936-4e7e-88f7-96311b3e3718">

**Dummy Akun: Qibas**
<img width="1338" alt="Screenshot 2024-09-22 at 12 39 03" src="https://github.com/user-attachments/assets/1a6a72e1-ea7a-49ea-a404-b328fdee10fb">

**Akun: Rifqi**
<img width="1316" alt="Screenshot 2024-09-22 at 12 46 31" src="https://github.com/user-attachments/assets/c345b09e-25ee-4473-83ba-e7f72bedc2df">

**Dummy Akun: Rifqi ** 
<img width="1321" alt="Screenshot 2024-09-22 at 12 46 15" src="https://github.com/user-attachments/assets/501fe8df-7343-413f-8e41-46a6e540bb92">


## Langkah-langkah Menghubungkan Model `Product` dengan `User`

1. Impor model user dari django
```bash
from django.contrib.auth.models import User
```

2. Membuat model product dengan foreignkey ke user
```bash
from django.db import models
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

foreignkey ini untuk menghubungkan setiap produk yang dibuat dengan user pengguna

3. Menjalankan perintah makemigrations dan migrate di terminal direktori

4. Membuat Produk di fungsi `create_product` sesuai masing-masing user dan diintegrasikan ke fungsi `show_main` untuk diambil dan disimpan berdasarkan user yang login
```bash
def show_main(request):
    product_entry = Product.objects.filter(user=request.user)
    ...

def create_product(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
    ...
```

5. Menampilkan Produk di Template `main.html`

## Langkah-langkah menampilkan informasi pengguna dan cookie `last_login`

1. `last_login` diset setelah pengguna berhasil login 
```bash
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now())) 
```

2. Ambil informasi pengguna yang login `request.user.username` 
```bash
def show_main(request):
    product_entry = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
```

3.Menampilkan informasi di Template `main.html`
```bash
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```






