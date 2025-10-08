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

   
## Tugas 5 (Tutorial)
1. Menambahkan file `toast.html` di direktori root dan mengisinya sebagai berikut untuk memunculkan bar notifikasi ketika melakukan delete, edit, logout, dan login.
   ```html
   <div id="toast-container" class="fixed top-5 right-5 z-[100] space-y-3">
    </div>

   <script>
       function showToast(message, type = 'success') {
           const container = document.getElementById('toast-container');
           if (!container) return;
   
           let bgColor, icon;
           if (type.includes('success')) {
               bgColor = 'bg-[#8B837A]';
               icon = '✅';
           } else if (type.includes('error')) {
               bgColor = 'bg-red-600';
               icon = '❌';
           } else if (type.includes('warning')) {
               bgColor = 'bg-yellow-600';
               icon = '⚠️';
           } else {
               bgColor = 'bg-gray-700';
               icon = '🔔';
           }
   
           const toast = document.createElement('div');
           toast.className = `p-4 rounded-md shadow-lg text-white max-w-xs transition-all duration-300 transform translate-x-full opacity-0 ${bgColor}`;
           toast.innerHTML = `<div class="flex items-center space-x-2"><span class="text-lg">${icon}</span><span class="font-medium text-sm">${message}</span></div>`;
           container.appendChild(toast);
   
           // Show
           setTimeout(() => {
               toast.classList.remove('translate-x-full', 'opacity-0');
               toast.classList.add('translate-x-0', 'opacity-100');
           }, 10); 
   
           // Hide
           setTimeout(() => {
               toast.classList.remove('translate-x-0', 'opacity-100');
               toast.classList.add('translate-x-full', 'opacity-0');
               toast.addEventListener('transitionend', () => toast.remove());
           }, 3000); 
       }
   
       // --- Logic to process Django messages on page load ---
       document.addEventListener('DOMContentLoaded', function() {
           {% if messages %}
               {% for message in messages %}
                   // message.tags contains 'success', 'error', 'warning', etc.
                   showToast('{{ message|safe }}', '{{ message.tags }}'); 
               {% endfor %}
           {% endif %}
       });
   </script>
   ```

2. Mengintegrasikan toast ke dalam `base.html` di direktori `templates` di root folder
   ```html
      ...
   <body>
       {% block content %}
   
       {% endblock %}
   
       {% include 'toast.html' %}
   </body>
   ...
   ```

3. Mengubah function `show_json()` untuk menampilkan data sekaligus melakukan perubahan di `main.html` di direktori `main`
   ```python
   def show_json(request):
    try:
        product_list = Product.objects.all()
        data = [
            {
                'id': product.name,
                'name': product.name,
                'price': product.price,             
                'description': product.description,
                'category': product.category,
                'thumbnail': product.thumbnail,
                'is_featured': product.is_featured,
                'brand': product.brand,
                'rating': float(product.rating),    
                'user_id': product.user_id,
                'user_username': product.user.username if product.user_id else None
            }
            for product in product_list
        ]

        return JsonResponse(data, safe=False)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    ```
3. Melakukan perubahan function `show_json_by_id` yang sudah ada di `views.py` sebagai berikut dan melakukan update template `product_detail.html` di direktori `main/templates`
   ```python
   def show_json_by_id(request, name):
    try:
        product = get_object_or_404(Product, pk=name)
        data = {
            'id': product.name,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'brand': product.brand,
            'rating': float(product.rating),
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else 'Unknown Seller',
        }

        return JsonResponse(data)
    
    except Exception as e:
        return JsonResponse({'detail': 'Product not found'}, status=404)
   ```
5. Menambahkan javaScript di `main.html` dan juga `product_detail.html`

6. Membuat `modal.html` di direktori `templates` yang berada di root
   ```python
      <div id="crudModal" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50">
     <div id="crudModalContent" class="bg-white rounded-lg shadow-lg w-5/6 sm:w-3/5 md:w-1/2 lg:w-2/5 xl:w-1/3 max-h-screen overflow-y-auto">
       <!-- Modal header -->
       <div class="flex items-center justify-between p-4 border-b">
         <div>
           <h3 class="text-xl font-semibold text-gray-900">
             Create New Product
           </h3>
           <p class="text-sm text-gray-600 mt-1">Share your sports product and stories with the community</p>
         </div>
         <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" onclick="hideModal()">
           <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
             <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
           </svg>
           <span class="sr-only">Close modal</span>
         </button>
       </div>
       <!-- Modal body -->
       <div class="px-6 py-4 space-y-6 form-style">
         <form id="productForm">
           <div class="mb-4">
             <label for="name" class="block text-sm font-medium text-gray-700">Product Name</label>
             <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2" placeholder="Enter product name" required>
           </div>
           <div class="mb-4">
             <label for="description" class="block text-sm font-medium text-gray-700">Content</label>
             <textarea id="description" name="description" rows="3" class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2" placeholder="Enter product description" required></textarea>
           </div>
           <div class="mb-4">
             <label for="category" class="block text-sm font-medium text-gray-700">Category</label>
             <select id="category" name="category" class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2" required>
               <option value="">Choose a category</option>
               <option value="transfer">Tas</option>
               <option value="update">Bola</option>
               <option value="exclusive">Sepatu</option>
               <option value="match">Baju</option>
               <option value="rumor">General</option>
             </select>
           </div>
   
           <div class="mb-4">
           <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
           <input type="number" id="price" name="price" step="0.01" min="0" 
                   class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2" 
                   placeholder="Enter product price" required>
           </div>
           
           <div class="mb-4">
             <label for="thumbnail" class="block text-sm font-medium text-gray-700">Thumbnail URL</label>
             <input type="url" id="thumbnail" name="thumbnail" class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2" placeholder="https://example.com/image.jpg">
           </div>
           <div class="mb-4">
             <div class="flex items-center">
               <input id="is_featured" name="is_featured" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded">
               <label for="is_featured" class="ml-2 text-sm font-medium text-gray-900">Featured Product</label>
             </div>
           </div>
         </form>
       </div>
       <!-- Modal footer -->
       <div class="flex flex-col sm:flex-row gap-4 p-6 border-t border-gray-200 rounded-b">
         <button type="button" id="cancelButton" class="order-2 sm:order-1 px-6 py-3 border border-gray-300 text-gray-700 rounded-md font-medium hover:bg-gray-50 transition-colors text-center" onclick="hideModal()">Cancel</button>
         <button type="submit" id="submitProduct" form="productForm" class="order-1 sm:order-2 flex-1 bg-green-600 text-white px-6 py-3 rounded-md font-medium hover:bg-green-700 transition-colors">Publish Product</button>
       </div>
     </div>
   </div>
   
   <script>
     function showModal() {
         const modal = document.getElementById('crudModal');
         const modalContent = document.getElementById('crudModalContent');
   
         modal.classList.remove('hidden'); 
         setTimeout(() => {
           modalContent.classList.remove('opacity-0', 'scale-95');
           modalContent.classList.add('opacity-100', 'scale-100');
         }, 50); 
     }
   
     function hideModal() {
         const modal = document.getElementById('crudModal');
         const modalContent = document.getElementById('crudModalContent');
   
         modalContent.classList.remove('opacity-100', 'scale-100');
         modalContent.classList.add('opacity-0', 'scale-95');
   
         setTimeout(() => {
           modal.classList.add('hidden');
         }, 150); 
     }
   
       async function addProductEntry() {
   
           await fetch("{% url 'main:add_product_entry_ajax' %}", {
           method: "POST",
           body: new FormData(document.querySelector('#productForm')),
           })
   
           document.getElementById("productForm").reset();
           hideModal();
           
           // Show toast notification
           showToast('Product added successfully!', '', 'success');
   
           // Dispatch custom event to notify main.html about new data
           document.dispatchEvent(new CustomEvent('productAdded'));
   
           return false;
       }
   
       document.getElementById("productForm").addEventListener("submit", function(e) {
           e.preventDefault();
           addProductEntry();
       })
   </script>
   ```
7. Menambahkan modal ke `base.html` ke `main.html`
   ```html
   ...
   <body>
       {% block content %}
   
       {% endblock %}
   
       {% include 'toast.html' %}
       {% include 'modal.html' %}
   </body>
   ...
   ```
8. Menambahkan fungsi `add_product_entry_ajax(request)` untuk menangani request ajax di `views.py`
   ```python
   @csrf_exempt
   @require_POST
   def add_product_entry_ajax(request):
       name = strip_tags(request.POST.get("name"))  
       description = strip_tags(request.POST.get("description"))  
       category = request.POST.get("category")
       thumbnail = request.POST.get("thumbnail")
       is_featured = request.POST.get("is_featured") == 'on'  
       price = request.POST.get("price")
       user = request.user
   
       new_product = Product(
           name=name,
           description=description,
           category=category,
           thumbnail=thumbnail,
           is_featured=is_featured,
           price=price,
           user=user,  
       )
       new_product.save()
   
       return HttpResponse(b"CREATED", status=201)

9. Tidak lupa untuk menambahkan URL pattern ke `main/urls.py`
   ```python
   urlpatterns = [
    ...
    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
   ]
   ```
10. Menambahkan fungsi JavaScript untuk AJAX dengan mengedit `modal.html`
    ```JavaScript
     async function addProductEntry() {

        await fetch("{% url 'main:add_product_entry_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#productForm')),
        })

        document.getElementById("productForm").reset();
        hideModal();
        
        // Show toast notification
        showToast('Product added successfully!', '', 'success');

        // Dispatch custom event to notify main.html about new data
        document.dispatchEvent(new CustomEvent('productAdded'));

        return false;
    }
    ```
11. Menambahkan event listener untuk mendeteksi ketika ada produk baru
    ```javascript
       <script>
      ...
      
      // Add event listener to detect new news
      document.addEventListener('productAdded', function() {
          // Refresh data without page reload
          fetchNewsFromServer();
      });
      </script>
    ```
12. Menambahkan `strip_tags` untuk membersihkan data baru di fungsi `add_product_entry_ajax()` di `views.py`
    ```python
      @csrf_exempt
      @require_POST
      def add_product_entry_ajax(request):
          name = strip_tags(request.POST.get("name"))  
          description = strip_tags(request.POST.get("description"))
    ....
    ```
13. Menambahkan DOMPurify di `base.html`
    ```html
      {% load static %}
      <!DOCTYPE html>
      <html lang="en">
        <head>
          ...
          <script src="https://cdn.tailwindcss.com"></script>
          <!-- Add DOMPurify here -->
          <script src="https://cdn.jsdelivr.net/npm/dompurify@3.0.5/dist/purify.min.js"></script>
          <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
        </head>
        ...
      </html>
    ```

## Tugas 6 (Pertanyaan)
**1.  Apa perbedaan antara synchronous request dan asynchronous request?**

Synchronous request berarti browser akan berhenti total untuk menunggu umpan balik atau respons dari server sebelum mengeksekus ikode atau interaksi dari pengguna. Sedangkan untuk asynchronous request berarti browser bisa terus jalan tanpa menunggu adanya respons sehingga UI masih tetap responsif 

**2. Bagaimana AJAX bekerja di Django (alur ruquest response)?**

Klien atau konteks di sini adalah browser, JS akan membuat objek atau menggunakan API untuk melakukan pengiriman HTTP ke suatu endpoint Django. Lalu server akan memproses rqeuest melalui view tanpa merender keseluruhan template HTML dan juga mengambil data dari database. Setelah itu akan diberikan respons dimana view mengembalikan data yang di program ini menggunakan JSON. Terakhir klien akan menerima kembali respons JSON dan halaman bisa diupdate.

**3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django>**

Keuntungan menggunakan AJAX adalah di bagian user expereience dan juga bandwith karena jika menggunakan AJAX, hanya bagian tertentu yang memang diperlukan yang dilakukan pengolahannya. Sehingga tidak perlu mentransfer keseluruhan HTML dan dapat mengurangi kecepatan waktu pemrosesan.

**4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur login dan register di Django?**

Kita dapat memanfaatkan penggunakan CSRF token dan juga HTTPS. Setiap request POST AJAX akan selalu menyertakan CSRF sehingga saat diproses, Django akan menerimanya. Juga, penggunaan HTTPS dapat membantu mengenkripsi data sensitf saat proses transfer data sehingga mengurangi peluang adanya penyalahgunaan

**5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?**

Dari User Experience (UX), AJAX paling berperan dengan membuat aplikasi web menjadi lebih cepat dan interaktif karena respons yang dibuatnya instan. Aplikasi web juga menjadi lebih dinamis untuk pengupdateannya karena diperbarui secara real time tanpa harus reload setiap ada perubahan.

