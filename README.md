# Sadjiw-Sporting-Goods
Ahmad Anggara Bayuadji Prawirosoenoto - 2406495514 - PBP A
https://ahmad-anggara41-sadjiwsportinggoods.pbp.cs.ui.ac.id/

## Tugas 4 (Tutorial)
1. Mengimplementasikan registrasi dengan menambahkan import sebagai berikut di `views.py` di direktori `main`
   ```python
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
   ```

2. Menambakan fungsi untuk register di `views.py` di direktori `main`
   ```python
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

3. Membuat berkas baru untuk menampilkan laman register dengan nama `register.html` di direktori `main/templates`

4. Mengimplementasikan login dnegna menambahkan import sebagai berikut di `views.py` di direktori `main`
   ```python
   from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
   from django.contrib.auth import authenticate, 
   ```

5. Menambahkan fungsi untuk login di `views.py` di direktori `main` dan sudah diintegrasikan dengan cookies untuk melihat last login
   ```python
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

6. Membuat berkas baru untuk menampilkan laman login dengan nama `login.html` di direktori `main/templates`

7. Mengimplementasikan logout dengan menambahkan import sebagai berikut di `views.py` di direktori `main`
   ```python
   from main.views import login_user
   ```

8. Menambahkan fungsi untuk login di `views.py` di direktori `main` dan sudah diintegrasikan dengan penghapusan cookies
   ```python
   def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
   ```

9. Melakukan penambahan path urls untuk register, login, dan logout di `urls.py` di direktori `main`
   ```python
   urlpatterns = [
    ....
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    ....
   ]
   ```

10. Menyalakan program dan buat dummy account dengan menuliskan berikut di terminal:
    ```bash
    python manage.py runserver

11. Melakukan penghubungan `Product` dengan `User` dengan menambahkan variabel `user` di class `Product` di `models.py`
    ```python
    class Product(models.Model):
      ....
      user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
      ....
    ```

12. Menambahkan tombol logout, informasi last login, dan juga button untuk melihat filter product my dan all di main.html di direktori `main/templates`
    ```html
    ....
    <a href="{% url 'main:logout' %}">
      <button>Logout</button>
    </a>
    
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    <hr>
      
    <a href="?filter=all">
        <button type="button">All Articles</button>
    </a>
    <a href="?filter=my">
        <button type="button">My Articles</button>
    </a>
    ....
    ```

13. Melakukan perubahan `show_main`, `create_product`, dan `show_product` agar memerlukan lopgin terlebih dahulu
    ```python
      @login_required(login_url='/login')
      def show_main(request):
          filter_type = request.GET.get("filter", "all")  # default 'all'
      
          if filter_type == "all":
              product_list = Product.objects.all()
          else:
              product_list = Product.objects.filter(user=request.user)
      
          context = {
              'npm': '240123456',
              'name': request.user.username,
              'class': 'PBP A',
              'product_list': product_list,
              'last_login': request.COOKIES.get('last_login', 'Never')
          }
          return render(request, "main.html",context)

      @login_required(login_url='/login')
      def create_product(request):
          form = ProductForm(request.POST or None)
      
          if form.is_valid() and request.method == 'POST':
              product_entry = form.save(commit = False)
              product_entry.user = request.user
              product_entry.save()
              return redirect('main:show_main')
      
          context = {
              'form': form
          }
      
          return render(request, "create_product.html", context)

      @login_required(login_url='/login')
      def show_product(request, name):
          product = get_object_or_404(Product, pk=name)
          
          context = {
              'product' : product
          }
          
          return render(request, "product_detail.html", context)
    ```

13. Melakukan migrations dan runserver
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

Tugas 4 (Pertanyaan)
---
**1. Apa itu Django `AuthenticationForm`? Jelaskan juga kelebihan dan kekurangannya.**

`AuthenticationForm` adalah class bawaan yang dapat mengecek apakah username dan password sudah cocok di database. Jika berhasil akan diteruskan untuk dibuatkan menjadi objek user. Keuntungannya adalah kita tidak perlu membuat fungsi autentikasi dari awal sehingga lebih praktis dan menghemat waktu. Namun, kekurangannya adalah tidak fleksibel dalam penggunaan variasi untuk login (misalnya dengan email) atau secara tampilan yang terlalu sederhana (perlu modifikasi lebih lanjut).

**2. Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?**

Perbedaannya adalah autentikasi lebih ke mencocokan data, misalnya mengecek apakah username dan password yang dimasukkan user sudah cocok. Sedangkan otorisasi memainkan peran dalam memberikan hak akses atau permission. Implementasi Django untuk kedua konsep tersebut pada konteks tugas ini adalah sebelum seorang user bisa mengakses websitenya perlu melakukan login, setelah itu oleh Django akan diautentikasi usernamenya dan passwordnya apakah sudah cocok, setelah itu oleh Django dilakukan pemberian otorisasi atau hak akses terhadap website.

**3. Apa saja kelebihan dan kekurangan _session_ dan _cookies_ dalam konteks menyimpan state di aplikasi web?**

Kelebihan cookies adalah mudah digunakan untuk menyimpan data sederhana di sisi browser. Namun, kekurangannya adalah cookies kurang aman karena bisa diubah langsung oleh user, juga ukurannya terbatas sekitar 4KB. Sedangkan session memiliki kelebihan dalam hal keamanan karena data sensitif disimpan di server bukan di browser, sehingga lebih sulit dimanipulasi oleh user. Selain itu session juga bisa menyimpan data yang lebih kompleks. Kekurangannya adalah session membutuhkan storage di server sehingga semakin banyak user yang aktif semakin berat pula beban server. 

**4. Apakah penggunaan _cookies_ aman secara _default_ dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**

Penggunaan cookies kurang aman karena pada dasarnya cookies disimpan langsung di browser. Hal itu menimbulkan risiko cookies tersebut bisa dimanipulasi oleh user secara langsung. Sehingga data yang ditampilan bisa saja tidak valid atau bahkan bisa dipakai untuk serangan XSS oleh pihak tidak bertanggung jawab. Django menanganinya dengna menyediakan fitur-fitur yang bisa memproteksi dari serangan seperti penggunaan secure cookies `CSRF_COOKIE_SECURE_` dan `SESSION_COOKIE_SECURE`.


## Tugas 5 (Tutorial)

1. Membuat direktori `static\css` dan menambahkan file `global.css`
   ```css
   .form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
   }
   .form-style form input:focus, form textarea:focus, form select:focus {
       outline: none;
       border-color: #16a34a;
       box-shadow: 0 0 0 3px #16a34a;
   }
   
   .form-style input[type="checkbox"] {
       width: 1.25rem;
       height: 1.25rem;
       padding: 0;
       border: 2px solid #d1d5db;
       border-radius: 0.375rem;
       background-color: white;
       cursor: pointer;
       position: relative;
       appearance: none;
       -webkit-appearance: none;
       -moz-appearance: none;
   }
   
   .form-style input[type="checkbox"]:checked {
       background-color: #16a34a;
       border-color: #16a34a;
   }
   
   .form-style input[type="checkbox"]:checked::after {
       content: '✓';
       position: absolute;
       top: 50%;
       left: 50%;
       transform: translate(-50%, -50%);
       color: white;
       font-weight: bold;
       font-size: 0.875rem;
   }
   
   .form-style input[type="checkbox"]:focus {
       outline: none;
       border-color: #16a34a;
       box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.1);
   }
   ```
2. Menkoneksikan tailwind ke aplikasi dengan mengubah isi dari `base.html` di `root/templates`
   ```html
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       {% block meta %} {% endblock meta %}
       <script src="https://cdn.tailwindcss.com"></script>
       <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
     </head>
     <body>
       {% block content %} {% endblock content %}
     </body>
   </html>
   ```

3. Menambahkan fitur baru yaitu `edit_product` di `views.py` di direktori `main`
   ```python
   def edit_product(request, name):
       news = get_object_or_404(Product, pk=name)
       form = ProductForm(request.POST or None, instance=news)
       if form.is_valid() and request.method == 'POST':
           form.save()
           return redirect('main:show_main')
   
       context = {
           'form': form
       }
   
       return render(request, "edit_product.html", context)
   ```
4. Menambahkan file `edit_product.html` di `main/templates` dan melakukan styling sesuai kebutuhan

5. Menambahkan fitur baru yaitu `delete_product` di `views.py` di direktori `main`
   ```python
   def delete_product(request, name):
       product = get_object_or_404(Product, pk=name)
       product.delete()
       return HttpResponseRedirect(reverse('main:show_main'))
   ```
6. Memasukkan path kedua fitur baru ke `urls.py` di direktori `main`
   ```python
   urlpatterns = [
       ...
       path('news/<str:name>/edit', edit_product, name='edit_product'),
       path('news/<str:name>/delete', delete_product, name='delete_product'),
   ]

7. Membuat navbar dengan menambahkan `navbar.html` di `templates` di direktori root sekaligus emmbuat styling

8. Melakukan styling ke semua html yang sudah dibuat sebelumnya (`create_product.html`, `login.html`, `main.html`, `product_detail.html` dan `register.html`) dan juga menambahkan html baru yaitu `card_product.html` untuk membuat card yang digunakan untuk menampilkan product
   
9. Tidak lupa untuk mengkonfigurasikan statiic files pada aplikasi dengan menambahkan di `settings.py` sebagai berikut:
```python
   ...
   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
       ...
   ]
   ...

   ...
   STATIC_URL = '/static/'
   if DEBUG:
       STATICFILES_DIRS = [
           BASE_DIR / 'static' # merujuk ke /static root project pada mode development
       ]
   else:
       STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
   ...
   ```

## Tugas 5 (Pertanyaan)
**1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

CSS selector ditentukan dengan konsep yang bernama spesifitas dimana semakin spesifik suatu selektor maka semakin tingga prioritasnya ketika digunakan ke elemen yang sama

| Selector | Example | Description | Weight |
|----------|---------|-------------|--------|
| Inline styles | `<h1 style="color: pink;">` | Highest priority, will override all other selectors | - |
| Id selectors | `#navbar` | Second highest priority | 1-0-0 |
| Classes, attribute selectors and pseudo-classes | `.test`, `[type="text"]`, `:hover` | Third highest priority | 0-1-0 |
| Elements and pseudo-elements | `h1`, `::before`, `::after` | Low priority | 0-0-1 |
| Universal selector and `:where()` | `*`, `:where()` | No priority | 0-0-0 |

**2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!**

Responsive design sangat penting karena membuat tampilan dan layout suatu aplikasi menjadi lebih dinamis dan tidak bergantung pada device (tidak statis). Sehingga jika dibuka dengan device lain tampilan aplikasi bisa menyesuaikan. Sedangkan jika tidak menerapkan responsive design, maka user bisa saja perlu menavigasi seperti zoom in zoom out hanya untuk mengakses sebuah fitur. Hal itu mengakibatkan pengalaman user menjadi tidak halus dan bisa saja malah meninggalkan aplikasi tersebut.

**3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

Secara umum, margin, border, dan padding bisa dikatakan sebagai pengatur ruangan di sekitar elemen. Margin merupakan ruang di luar border yang memisahkan elemen dari elemen lain, border merupakan garis tepi elemen yang berada di antara padding dan margin, dan padding adalah ruangan di dalam border yang memisahkan konten elemen dari tepi elemen. Jika digambarkan maka akan menghasilkan ruangan seperti ini:

<img width="393" height="240" alt="image" src="https://github.com/user-attachments/assets/a7422ac3-9248-4ef7-be5a-146bf29bd620" />

sumber: https://www.google.com/url?sa=i&url=https%3A%2F%2Fid.pinterest.com%2Fpin%2Fhow-are-margins-borders-padding-and-content-related-web-tutorials--426856870909031540%2F&psig=AOvVaw2CcrKDB2UaEfOCFg6E01Sf&ust=1759375310740000&source=images&cd=vfe&opi=89978449&ved=0CBgQjhxqFwoTCODq6_SFgpADFQAAAAAdAAAAABAE

**4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

Flex box dan grid merupakan konsep untuk mengatur layout di CSS. Flex Box mengatur elemen satu dimensi, jadi hanya berupa baris ATAU kolom untuk mengatur jarak, posisi, atau ukuran suatu elemen. Contohnya adalah menu navigasi ataupun card. Sedangkan untuk grid, ia mengatur elemen secara dua dimensi jadi berupa baris DAN kolom. Contohnya adalah untuk pembuatan galeri ataupun dashboard.

   
   
   
