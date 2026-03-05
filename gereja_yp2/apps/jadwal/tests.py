from django.test import TestCase
from django.urls import reverse

from .models import JadwalMisa


class JadwalMisaModelTest(TestCase):
    def setUp(self):
        self.jadwal = JadwalMisa.objects.create(
            nama_misa='Misa Mingguan',
            hari='2026-01-05',
            waktu='07:00:00',
        )

    def test_str_representation(self):
        self.assertIn('Misa Mingguan', str(self.jadwal))


class JadwalMisaViewTest(TestCase):
    def test_jadwal_misa_returns_200(self):
        response = self.client.get(reverse('jadwal_misa'))
        self.assertEqual(response.status_code, 200)

    def test_jadwal_petugas_returns_200(self):
        response = self.client.get(reverse('jadwal_petugas'))
        self.assertEqual(response.status_code, 200)
