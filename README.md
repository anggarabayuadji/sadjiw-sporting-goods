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
    ```
   DB_NAME=<nama database>
   DB_HOST=<host database>
   DB_PORT=<port database>
   DB_USER=<username database>
   DB_PASSWORD=<password database>
   SCHEMA=tutorial
   PRODUCTION=True
10. Melakukan modifikasi di `settings.py` 
