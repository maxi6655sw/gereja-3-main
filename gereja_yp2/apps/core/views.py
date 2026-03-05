from django.shortcuts import render, redirect
from django.contrib.auth import logout

from apps.berita.services import get_random_berita


def index(request):
    """Homepage — shows randomly selected news articles."""
    berita_acak = get_random_berita(count=3)
    return render(request, 'core/index.html', {'berita_acak': berita_acak})


def home(request):
    """Homepage — shows randomly selected news articles."""
    berita_acak = get_random_berita(count=3)
    return render(request, 'core/home.html', {'berita_acak': berita_acak})


def logout_view(request):
    logout(request)
    return redirect('/')
