# Sadjiw-Sporting-Goods
Ahmad Anggara Bayuadji Prawirosoenoto - 2406495514 - PBP A
https://ahmad-anggara41-sadjiwsportinggoods.pbp.cs.ui.ac.id/

## Tugas 4
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

13. Melakukan migrations dan runserver
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```



    
   
   
   
