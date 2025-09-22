# Sadjiw-Sporting-Goods
Ahmad Anggara Bayuadji Prawirosoenoto - 2406495514 - PBP A
https://ahmad-anggara41-sadjiwsportinggoods.pbp.cs.ui.ac.id/

## Tugas 4
Tutorial
---
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

Pertanyaan
---
**1. Apa itu Django `AuthenticationForm`? Jelaskan juga kelebihan dan kekurangannya.**

`AuthenticationForm` adalah class bawaan yang dapat mengecek apakah username dan password sudah cocok di database. Jika berhasil akan diteruskan untuk dibuatkan menjadi objek user. Keuntungannya adalah kita tidak perlu membuat fungsi autentikasi dari awal sehingga lebih praktis dan menghemat waktu. Namun, kekurangannya adalah tidak fleksibel dalam penggunaan variasi untuk login (misalnya dengan email) atau secara tampilan yang terlalu sederhana (perlu modifikasi lebih lanjut).

**2. Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?**

Perbedaannya adalah autentikasi lebih ke mencocokan data, misalnya mengecek apakah username dan password yang dimasukkan user sudah cocok. Sedangkan otorisasi memainkan peran dalam memberikan hak akses atau permission. Implementasi Django untuk kedua konsep tersebut pada konteks tugas ini adalah sebelum seorang user bisa mengakses websitenya perlu melakukan login, setelah itu oleh Django akan diautentikasi usernamenya dan passwordnya apakah sudah cocok, setelah itu oleh Django dilakukan pemberian otorisasi atau hak akses terhadap website.

**3. Apa saja kelebihan dan kekurangan _session_ dan _cookies_ dalam konteks menyimpan state di aplikasi web?**

Kelebihan cookies adalah mudah digunakan untuk menyimpan data sederhana di sisi browser. Namun, kekurangannya adalah cookies kurang aman karena bisa diubah langsung oleh user, juga ukurannya terbatas sekitar 4KB. Sedangkan session memiliki kelebihan dalam hal keamanan karena data sensitif disimpan di server bukan di browser, sehingga lebih sulit dimanipulasi oleh user. Selain itu session juga bisa menyimpan data yang lebih kompleks. Kekurangannya adalah session membutuhkan storage di server sehingga semakin banyak user yang aktif semakin berat pula beban server. 

**4. Apakah penggunaan _cookies_ aman secara _default_ dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**

Penggunaan cookies kurang aman karena pada dasarnya cookies disimpan langsung di browser. Hal itu menimbulkan risiko cookies tersebut bisa dimanipulasi oleh user secara langsung. Sehingga data yang ditampilan bisa saja tidak valid atau bahkan bisa dipakai untuk serangan XSS oleh pihak tidak bertanggung jawab. Django menanganinya dengna menyediakan fitur-fitur yang bisa memproteksi dari serangan seperti penggunaan secure cookies `CSRF_COOKIE_SECURE_` dan `SESSION_COOKIE_SECURE`.




   
   
   
