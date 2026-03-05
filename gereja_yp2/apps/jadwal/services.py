"""
Business logic / service layer for the Jadwal (Schedule) app.
"""

from .models import JadwalMisa


def get_all_jadwal_misa():
    """Return all JadwalMisa entries ordered by hari and waktu."""
    return JadwalMisa.objects.order_by('hari', 'waktu')
