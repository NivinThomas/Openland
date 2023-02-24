from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='Welcome'),
    path('Register',views.register,name='Register'),
    path('Listings',views.listings,name='Listings'),
    path('Search',views.search,name='Search'),
    path('Login',views.usr_login,name='Login'),
    path('New',views.new,name='New'),
]
