from django.shortcuts import render

from . import services


def jadwal_misa(request):
    """Display mass schedule."""
    jadwal = services.get_all_jadwal_misa()
    return render(request, 'jadwal/jadwal_misa.html', {'jadwal': jadwal})


def jadwal_petugas(request):
    """Display weekly duty schedule."""
    return render(request, 'jadwal/jadwal_petugas.html')
