from django.contrib import admin
from django.utils.html import format_html
from .models import JadwalMisa
from .models import Berita, Kategori

@admin.register(JadwalMisa)
class JadwalMisaAdmin(admin.ModelAdmin):
    list_display = ('nama_misa', 'hari', 'waktu', 'tampilkan_gambar')
    list_filter = ('hari',)
    search_fields = ('nama_misa',)
    ordering = ('hari', 'waktu')

    def tampilkan_gambar(self, obj):
        if obj.gambar:
            return format_html(
                '<img src="{}" width="70" height="70" style="object-fit: cover; border-radius: 8px;" />',
                obj.gambar.url
            )
        return "Tidak ada gambar"
    tampilkan_gambar.short_description = "Gambar"

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('nama',)
    prepopulated_fields = {'slug': ('nama',)}

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'tanggal', 'penulis')
    list_filter = ('kategori', 'tanggal')
    search_fields = ('judul', 'isi')
    prepopulated_fields = {'slug': ('judul',)}

class CustomAdminSite(admin.AdminSite):
    site_header = "Administrasi Gereja Santo Yohanes Paulus II"
    site_title = "Admin Gereja YP2"
    index_title = "Dashboard Admin"
    index_template = 'admin/index.html'

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        # Custom app list if needed
        return app_list

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['total_berita'] = Berita.objects.count()
        extra_context['total_kategori'] = Kategori.objects.count()
        extra_context['total_jadwal_misa'] = JadwalMisa.objects.count()
        extra_context['recent_berita'] = Berita.objects.order_by('-tanggal')[:5]

        # Data for category chart
        from django.db.models import Count
        category_counts = Kategori.objects.annotate(berita_count=Count('berita')).values('nama', 'berita_count')
        category_data = {
            'labels': [cat['nama'] for cat in category_counts],
            'data': [cat['berita_count'] for cat in category_counts]
        }
        extra_context['category_data'] = category_data

        return super().index(request, extra_context)

# Create instance
admin_site = CustomAdminSite(name='custom_admin')

# Register models with custom admin site
admin_site.register(JadwalMisa, JadwalMisaAdmin)
admin_site.register(Kategori, KategoriAdmin)
admin_site.register(Berita, BeritaAdmin)
