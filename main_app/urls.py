from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contact_us_page, name='contact-us'),

    path('categories/', views.categories_list, name='categories-list'),
    path('categories/<str:filter_by_name>/', views.products_list, name='products-list'),
    path('categories/<str:category_name>/<str:product_name>/', views.product_view, name='product-view'),

    path('manufactures/', views.manufactures_list, name='manufactures-list'),
    path('manufactures/<str:filter_by_name>/', views.products_list, name='products-list-by-manufacture'),
    path('manufactures/<str:filter_by_name>/<str:product_name>/',
         views.product_view, name='product-view-by-manufacture'),

    path('campaign/', views.campaign_list, name='campaign_list'),
    path('campaign/<str:pk>/', views.campaign_view, name='campaign_view'),

    path('search/', views.search, name='search'),
    
]
