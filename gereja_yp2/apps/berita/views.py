from django.shortcuts import render

from . import services


def kilas_berita(request):
    """Display all news articles."""
    berita_list = services.get_all_berita()
    return render(request, 'berita/kilas_berita.html', {'berita_list': berita_list})


def detail_berita(request, slug):
    """Display a single news article and its related articles."""
    berita = services.get_berita_by_slug(slug)
    berita_terkait = services.get_berita_terkait(berita)
    return render(request, 'berita/detail_berita.html', {
        'berita': berita,
        'berita_terkait': berita_terkait,
    })
