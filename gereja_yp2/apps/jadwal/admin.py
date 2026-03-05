from django.contrib import admin
from django.utils.html import format_html

from config.admin_site import admin_site
from .models import JadwalMisa
from django import forms

class JadwalMisaAdminForm(forms.ModelForm):
    class Meta:
        model = JadwalMisa
        fields = '__all__'
        widgets = {
            'waktu': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'vTimeField',
                    }, 
                    format='%H:%M'
                ),
        }

@admin.register(JadwalMisa, site=admin_site)
class JadwalMisaAdmin(admin.ModelAdmin):
    form = JadwalMisaAdminForm
    # ── List view ──────────────────────────────────────────────────────────
    list_display  = ('thumbnail', 'nama_misa', 'hari_format', 'waktu_format')
    list_display_links = ('thumbnail', 'nama_misa')
    search_fields = ('nama_misa',)
    date_hierarchy = 'hari'
    list_per_page  = 20

    # ── Form ───────────────────────────────────────────────────────────────
    save_on_top = True
    readonly_fields = ('pratinjau_gambar',)

    fieldsets = (
        ('📋 Detail Misa', {
            'fields': ('nama_misa', 'hari', 'waktu'),
        }),
        ('🖼️ Gambar', {
            'fields': ('gambar', 'pratinjau_gambar'),
            'classes': ('collapse',),
            'description': 'Upload gambar untuk jadwal misa (opsional).',
        }),
    )

    # ── Custom columns ─────────────────────────────────────────────────────
    def thumbnail(self, obj):
        if obj.gambar:
            return format_html(
                '<img src="{}" width="48" height="48" style="object-fit:cover;border-radius:8px;box-shadow:0 1px 4px rgba(0,0,0,.2);" />',
                obj.gambar.url,
            )
        return format_html('<span style="color:#adb5bd;font-size:18px;"><i class="fas fa-calendar-alt"></i></span>')
    thumbnail.short_description = ''

    def hari_format(self, obj):
        return format_html(
            '<span style="font-weight:600;">{}</span>',
            obj.hari.strftime('%A, %d %B %Y') if obj.hari else '—',
        )
    hari_format.short_description = 'Hari'
    hari_format.admin_order_field = 'hari'

    def waktu_format(self, obj):
        return format_html(
            '<span style="background:#17a2b8;color:#fff;padding:2px 10px;border-radius:12px;font-size:12px;font-weight:600;">⏰ {}</span>',
            obj.waktu.strftime('%H:%M') if obj.waktu else '—',
        )
    waktu_format.short_description = 'Waktu'
    waktu_format.admin_order_field = 'waktu'

    def pratinjau_gambar(self, obj):
        if obj.gambar:
            return format_html(
                '<img src="{}" style="max-width:320px;border-radius:10px;box-shadow:0 2px 8px rgba(0,0,0,.15);" />',
                obj.gambar.url,
            )
        return 'Belum ada gambar.'
    pratinjau_gambar.short_description = 'Pratinjau'
