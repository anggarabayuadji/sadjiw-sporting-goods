from django.urls import path
from main.views import *
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:name>/', show_product, name='show_product'),
    path('json/', show_json, name='show_json'),
    path('json/<str:name>/', show_json_by_id, name='show_json_by_id'),
    path('xml/<str:name>/', show_xml_by_id, name='show_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('news/<str:name>/edit', edit_product, name='edit_product'),
    path('news/<str:name>/delete', delete_product, name='delete_product'),
    path('create-product-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
]
