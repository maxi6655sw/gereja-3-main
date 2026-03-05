from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html

from config.admin_site import admin_site
from .models import Berita, Kategori


@admin.register(Kategori, site=admin_site)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('nama', 'slug', 'jumlah_berita')
    prepopulated_fields = {'slug': ('nama',)}
    search_fields = ('nama',)
    ordering = ('nama',)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(berita_count=Count('berita'))

    def jumlah_berita(self, obj):
        count = obj.berita_count
        color = '#28a745' if count > 0 else '#6c757d'
        return format_html(
            '<span style="background:{};color:#fff;padding:2px 10px;border-radius:12px;font-size:12px;font-weight:600;">{} berita</span>',
            color, count,
        )
    jumlah_berita.short_description = 'Jumlah Berita'
    jumlah_berita.admin_order_field = 'berita_count'


@admin.register(Berita, site=admin_site)
class BeritaAdmin(admin.ModelAdmin):
    # ── List view ──────────────────────────────────────────────────────────
    list_display  = ('thumbnail', 'judul', 'badge_kategori', 'penulis', 'tanggal')
    list_display_links = ('thumbnail', 'judul')
    list_filter   = ('kategori', 'tanggal', 'penulis')
    search_fields = ('judul', 'isi', 'penulis')
    date_hierarchy = 'tanggal'
    list_per_page  = 15
    list_select_related = ('kategori',)
    autocomplete_fields = ['kategori']

    # ── Form ───────────────────────────────────────────────────────────────
    save_on_top = True
    prepopulated_fields = {'slug': ('judul',)}
    readonly_fields = ('ringkasan', 'pratinjau_gambar')

    fieldsets = (
        ('📝 Informasi Utama', {
            'fields': ('judul', 'slug', 'kategori', 'penulis', 'tanggal'),
        }),
        ('🖼️ Gambar', {
            'fields': ('gambar', 'pratinjau_gambar'),
            'classes': ('collapse',),
            'description': 'Upload gambar untuk artikel (opsional).',
        }),
        ('📄 Konten', {
            'fields': ('isi',),
        }),
        ('🔍 Ringkasan & SEO', {
            'fields': ('ringkasan',),
            'classes': ('collapse',),
            'description': 'Ringkasan diisi otomatis dari 250 karakter pertama jika dikosongkan.',
        }),
    )

    # ── Custom columns ─────────────────────────────────────────────────────
    def thumbnail(self, obj):
        if obj.gambar:
            return format_html(
                '<img src="{}" width="52" height="52" style="object-fit:cover;border-radius:8px;box-shadow:0 1px 4px rgba(0,0,0,.2);" />',
                obj.gambar.url,
            )
        return format_html('<span style="color:#adb5bd;font-size:20px;"><i class="fas fa-image"></i></span>')
    thumbnail.short_description = ''

    def badge_kategori(self, obj):
        if obj.kategori:
            return format_html(
                '<span style="background:#007bff;color:#fff;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600;">{}</span>',
                obj.kategori.nama,
            )
        return format_html('<span style="color:#adb5bd;">—</span>')
    badge_kategori.short_description = 'Kategori'
    badge_kategori.admin_order_field = 'kategori__nama'

    def pratinjau_gambar(self, obj):
        if obj.gambar:
            return format_html(
                '<img src="{}" style="max-width:320px;border-radius:10px;box-shadow:0 2px 8px rgba(0,0,0,.15);" />',
                obj.gambar.url,
            )
        return 'Belum ada gambar.'
    pratinjau_gambar.short_description = 'Pratinjau'
