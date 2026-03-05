from django.urls import path

from . import views

urlpatterns = [
    path('misa/', views.jadwal_misa, name='jadwal_misa'),
    path('petugas/', views.jadwal_petugas, name='jadwal_petugas'),
]
