from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('jadwal_misa/', views.jadwal_misa, name='jadwal_misa'),
    path('jadwal_petugas/', views.jadwal_petugas, name='jadwal_petugas'),
    path('kilas_berita/', views.kilas_berita, name='kilas_berita'),
    path('berita/<slug:slug>/', views.detail_berita, name='detail_berita'),
    path('berita/kategori/<slug:slug>/', views.kilas_berita, name='kilas_berita_kategori'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
