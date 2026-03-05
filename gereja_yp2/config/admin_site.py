"""
Shared custom admin site for the gereja_yp2 project.
All apps register their models here via their own admin.py files.
"""

from django.contrib import admin
from django.db.models import Count


class CustomAdminSite(admin.AdminSite):
    site_header = "Administrasi Gereja Santo Yohanes Paulus II"
    site_title = "Admin Gereja YP2"
    index_title = "Dashboard Admin"
    index_template = 'admin/index.html'

    def get_app_list(self, request, app_label=None):
        return super().get_app_list(request, app_label)

    def index(self, request, extra_context=None):
        # Import here to avoid circular imports at module load time
        from apps.berita.models import Berita, Kategori
        from apps.jadwal.models import JadwalMisa

        extra_context = extra_context or {}
        extra_context['total_berita'] = Berita.objects.count()
        extra_context['total_kategori'] = Kategori.objects.count()
        extra_context['total_jadwal_misa'] = JadwalMisa.objects.count()
        extra_context['recent_berita'] = Berita.objects.order_by('-tanggal')[:5]

        category_counts = (
            Kategori.objects
            .annotate(berita_count=Count('berita'))
            .values('nama', 'berita_count')
        )
        extra_context['category_data'] = {
            'labels': [cat['nama'] for cat in category_counts],
            'data': [cat['berita_count'] for cat in category_counts],
        }

        return super().index(request, extra_context)


# Singleton custom admin site used across all apps
admin_site = CustomAdminSite(name='custom_admin')
