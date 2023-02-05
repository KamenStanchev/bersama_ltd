from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contact_us_page, name='contact-us'),
    path('categories/', views.categories_list, name='categories-list'),
    path('categories/<str:category_name>/', views.products_list, name='products-list'),
    path('categories/<str:category_name>/<str:product_name>/', views.product_view, name='product-view'),
    path('search/', views.search, name='search'),
    
]
