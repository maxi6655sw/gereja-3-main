from django.urls import path

from . import views

urlpatterns = [
    path('', views.kilas_berita, name='kilas_berita'),
    path('<slug:slug>/', views.detail_berita, name='detail_berita'),
    path('kategori/<slug:slug>/', views.kilas_berita, name='kilas_berita_kategori'),
]
