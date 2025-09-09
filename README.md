# Sadjiw-Sporting-Goods
Tugas Individu Pemrograman Berbasis Platform 

oleh Ahmad Anggara Bayuadji Prawirosenoto - PBP A - 2406495514 - https://ahmad-anggara41-sadjiwsportinggoods.pbp.cs.ui.ac.id/

Langkah-langkah pembuatan:

1. Membuat repositori baru di Github
2. Clone repositori yang telah dibuat ke local
3. Menyiapakan virtual environment dengan cara membuka direktori proyek lalu membuka cmd dan menuliskan sebagai berikut:
   ```bash
   python -m venv env

4. Menyalakan virtual environment untuk mengisolasi package dan dependencies dengan menulis kode berikut di cmd
   ```bash
   env\Scripts\activate

5. Menyiapkan dependencies dengan membuat requirements.txt di direktori projek dengan isi sebagai berikut
   ```
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   python-dotenv
6. Melakukan instalasi dependencies
   ```bash
   pip install -r requirements.txt
            
7. Membuat proyek django
   ```bash
   django-admin startproject Sadjiw_Sporting_Goods .

8. Menambahkan konfigurasi `SETTINGS=False` di file `.env`

9. Membuat file `.env.prod` dan mengisinya dengan kredensial database yang diberikan di email
    ```python
   DB_NAME=<nama database>
   DB_HOST=<host database>
   DB_PORT=<port database>
   DB_USER=<username database>
   DB_PASSWORD=<password database>
   SCHEMA=tutorial
   PRODUCTION=True
10. Melakukan modifikasi di `settings.py` untuk menggunakan environment variables
    ```python
    import os
    from dotenv import load_dotenv
    # Load environment variables from .env file
    load_dotenv()
11. Menambahkan `ALLOWED_HOST` di `settings.py`
    ```python
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
12. Menambahkan konfigurasi `PRODUCTION` di atas code `DEBUG` di `settings.py`
    ```python
    PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'
13. Menrubah konfigurasi database di `settings.py`
    ```python
      # Database configuration
      if PRODUCTION:
       # Production: gunakan PostgreSQL dengan kredensial dari environment variables
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.postgresql',
               'NAME': os.getenv('DB_NAME'),
               'USER': os.getenv('DB_USER'),
               'PASSWORD': os.getenv('DB_PASSWORD'),
               'HOST': os.getenv('DB_HOST'),
               'PORT': os.getenv('DB_PORT'),
               'OPTIONS': {
                   'options': f"-c search_path={os.getenv('SCHEMA', 'public')}"
               }
           }
       }
      else:
       # Development: gunakan SQLite
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.sqlite3',
               'NAME': BASE_DIR / 'db.sqlite3',
           }
       }
14. Membuat aplikasi `main` dengan menulis di terminal:
    ```bash
    python manage.py startapp main
15. Menambahkan `'main'` ke dalam `INSTALLED_APPS` di `settings.py`
    ```python
    INSTALLED_APPS = [
    ...,
    'main'
    ]
16. Melakukan routing dengan mengubah `urls.py` yang berada di direktori `sadjiw_sporting_goods` dengan kode berikut:
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    ]
17. Melakukan perubahan di `models.py` menjadi:
    ```python
    class Product(models.Model):    
       name = models.CharField(max_length=255)
       price = models.IntegerField
       description = models.TextField
       thumbnail = models.URLField
       category = models.CharField
       is_featured = models.BooleanField
       brand = models.CharField
       rating = models.DecimalField(default=0.0, max_digits=5, decimal_places=1)
18. Memastikan Django dapat melacak perubahan mode di basis data dengan cara melakukan migrasi melalui cmd
    ```bash
    python manage.py migrations
    ```
    ```bash
    python manage.py migrate
19. Melakukan penambahan direktori `template` di `main`
20. Membuat `main.html` di dalam direktori `template` untuk laman `main`
    ```python
    <h1>Sadjiw Sporting Goods</h1>

    <h5>Name: <h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}</p>
21. Menembahkan fungsi untuk merender `main.html` yang sudah dibuat tadi
    ```python
    def show_main(request):
       context = {
           'name': 'Ahmad Anggara Bayuadji Prawirosoenoto',
           'class': 'PBP A'
       }
   
       return render(request, "main.html", context)
22. Melakukan routing `urls.py` pada aplikasi `main`:
    ```python
    from django.urls import path
    from main.views import show_main
   
    app_name = 'main'
   
    urlpatterns = [
       path('', show_main, name='show_main'),
    ]
23. Melakukan deployment ke PWS dengan menambahkan URL deployment PWS pada `ALLOWED_HOST` di `settings.py`
    ```python
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "ahmad-anggara41-sadjiwsportinggoods.pbp.cs.ui.ac.id"]
24. Melakukan project command yang berada di PWS:
    ```bash
    git remode add pws ahmad-anggara41-sadjiwsportinggoods.pbp.cs.ui.ac.id
    git branch -M master
    git push pws master
25. Cek keberhasilan web dengan membuka link [ini](https://ahmad-anggara41-sadjiwsportinggoods.pbp.cs.ui.ac.id/)


Pertanyaan:

**1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.**
<img width="762" height="424" alt="image" src="https://github.com/user-attachments/assets/4882741f-3a73-4e7d-8f84-892036bae51a" />

Saat user mengirimkan request ke server, Django akan memeriksa urls.py untuk menentukan view yang sesuai. Lalu, request diteruskan ke views.py yang menjalankan logika aplikasi. Jika diperlukan akses data, views.py akan berinteraksi dengan models.py untuk membaca atau menulis ke database. Data yang diperoleh kemudian diproses di views.py dan diteruskan ke template untuk dirender menjadi halaman HTML. Hasil akhirnya dikembalikan ke server dan ditampilkan kepada user.

**2. Jelaskan peran `settings.py` dalam proyek Django!**

   `settings.py` digunakan untuk mengkonfigurasi aplikasi yang kita buat. `settings.py` akan menentukan bagaimana sifat dari aplikasi kita saat dijalankan.
   Contoh hal yang bisa dikonfigurasikan adalah seperti database, INSTALLED_APPS untuk mendaftarkan modul yang digunakan, TEMPLATES untuk mengatur file HTML template, ALLOWED_HOSTS untuk menentukan domain/host yang diizinkan, dan lain sebagainya.

**3. Bagaimana cara kerja migrasi database di Django?**
Saat developer melakukan perubahan pada model di `models.py`, Django menggunakan perintah `makemigration` untuk membuat file yang berisi instruksi perubahan. SEtelah itu, perlu diikuti dengan perintah `migrate` agar Django dapat mengeksekusi instruksi tersebut ke database sehingga developer tidak perlu menulis SQL secara manual

**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
Menurut saya, framework Django digunakan karena yang pertama adalah penggunaan bahasa pemrogramannya yaoti Python. Hal itu dikarenakan python lebih mudah untuk dibaca secara langsung dibandingkan bahasa lainnya. Kedua, Django sudah memiliki banyak dokumentasi yang bertebaran di internet, sehingga untuk memelajarinya juga jauh lebih mudah. Ketiga, Django memiliki struktur yang jelas, termasuk menggunakan pola MTV sehingga membantu kami sebagai pemula punya gambaran alur yang digunakan. 

**Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?**
Dari saya pribadi tidak ada, pengadaan tutorial sudah sangat baik dan asdos sudah sangat membantu dan selalu menangani sebuah masalah yang dihadapi dengan cepat. Semangat terus ya asdos untuk mengahadapi kita hehe
