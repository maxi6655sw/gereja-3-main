from django.db import models


class JadwalMisa(models.Model):
    nama_misa = models.CharField(max_length=100)
    hari = models.DateField()
    waktu = models.TimeField()
    gambar = models.ImageField(upload_to='jadwal/', blank=True, null=True)

    class Meta:
        verbose_name = 'Jadwal Misa'
        verbose_name_plural = 'Jadwal Misa'
        ordering = ['hari', 'waktu']

    def __str__(self):
        return f"{self.nama_misa} ({self.hari})"
