"""
Business logic / service layer for the Berita (News) app.
Views should call these functions instead of querying the ORM directly.
"""

import random

from .models import Berita, Kategori


def get_all_berita():
    """Return all berita ordered by newest first."""
    return Berita.objects.select_related('kategori').order_by('-tanggal')


def get_berita_by_slug(slug: str) -> Berita:
    """Return a single Berita instance by slug (raises 404 if missing)."""
    from django.shortcuts import get_object_or_404
    return get_object_or_404(Berita.objects.select_related('kategori'), slug=slug)


def get_berita_terkait(berita: Berita, count: int = 3):
    """Return related berita from the same category, excluding the given one."""
    if berita.kategori:
        return (
            Berita.objects.filter(kategori=berita.kategori)
            .exclude(pk=berita.pk)
            .order_by('-tanggal')[:count]
        )
    return Berita.objects.exclude(pk=berita.pk).order_by('-tanggal')[:count]


def get_random_berita(count: int = 3):
    """Return a randomly selected list of berita (used on the homepage)."""
    all_berita = list(Berita.objects.all())
    return random.sample(all_berita, min(len(all_berita), count))


def get_all_kategori():
    """Return all kategori."""
    return Kategori.objects.all()
