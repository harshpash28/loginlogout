from django.contrib import admin
from django.urls import path
from loginapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index),
    path('register',views.uregister),
    path('login',views.ulogin),
    path('logout',views.ulogout),
]