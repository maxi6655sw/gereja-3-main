from django.shortcuts import render
from .models import JadwalMisa
from .models import Berita, Kategori
from django.shortcuts import render, get_object_or_404
import random
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')

def jadwal_petugas(request):
    return render(request, 'jadwal_petugas.html')

def jadwal_misa(request):
    jadwal = JadwalMisa.objects.all().order_by('hari', 'waktu')
    return render(request, 'jadwal_misa.html', {'jadwal': jadwal})

def kilas_berita(request):
    berita_list = Berita.objects.all().order_by('-tanggal')
    return render(request, 'kilas_berita.html', {'berita_list': berita_list})



def detail_berita(request, slug):
    berita = get_object_or_404(Berita, slug=slug)

    if berita.kategori:
        berita_terkait = (
            Berita.objects.filter(kategori=berita.kategori)
            .exclude(id=berita.id)
            .order_by('-tanggal')[:3]
        )
    else:
        berita_terkait = Berita.objects.exclude(id=berita.id).order_by('-tanggal')[:3]

    return render(request, 'detail_berita.html', {
        'berita': berita,
        'berita_terkait': berita_terkait
    })


def home(request):
    # Ambil semua berita lalu pilih 3 secara acak
    semua_berita = list(Berita.objects.all())
    berita_acak = random.sample(semua_berita, min(len(semua_berita), 3))

    return render(request, 'home.html', {
        'berita_acak': berita_acak
    })

def logout_view(request):
    logout(request)
    return redirect('/')
