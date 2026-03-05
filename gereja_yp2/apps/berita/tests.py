from django.test import TestCase
from django.urls import reverse

from .models import Berita, Kategori


class BeritaModelTest(TestCase):
    def setUp(self):
        self.kategori = Kategori.objects.create(nama='Kegiatan')
        self.berita = Berita.objects.create(
            judul='Berita Test',
            isi='Isi berita test yang panjang.',
            penulis='Admin',
            kategori=self.kategori,
        )

    def test_slug_auto_generated(self):
        self.assertEqual(self.berita.slug, 'berita-test')

    def test_ringkasan_auto_generated(self):
        self.assertIsNotNone(self.berita.ringkasan)

    def test_str_returns_judul(self):
        self.assertEqual(str(self.berita), 'Berita Test')


class KilasBeritaViewTest(TestCase):
    def test_page_returns_200(self):
        response = self.client.get(reverse('kilas_berita'))
        self.assertEqual(response.status_code, 200)

    def test_detail_returns_404_for_unknown_slug(self):
        response = self.client.get(reverse('detail_berita', args=['tidak-ada']))
        self.assertEqual(response.status_code, 404)
