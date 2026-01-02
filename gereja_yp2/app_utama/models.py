from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class JadwalMisa(models.Model):
    nama_misa = models.CharField(max_length=100)
    hari = models.CharField(max_length=20)
    waktu = models.TimeField()
    gambar = models.ImageField(upload_to='jadwal/', blank=True, null=True)

    def __str__(self):
        return f"{self.nama_misa} ({self.hari})"

class Kategori(models.Model):
    nama = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    gambar = models.ImageField(upload_to='berita/', blank=True, null=True)
    isi = models.TextField()
    ringkasan = models.TextField(blank=True, null=True)
    tanggal = models.DateField(default=timezone.now)
    penulis = models.CharField(max_length=100, default="Admin")
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, related_name="berita")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        if not self.ringkasan:
            self.ringkasan = self.isi[:250]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.judul