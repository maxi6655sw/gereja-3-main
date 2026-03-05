"""
Root URL configuration for gereja_yp2 project.
"""

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.admin_site import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('apps.core.urls')),
    path('berita/', include('apps.berita.urls')),
    path('jadwal/', include('apps.jadwal.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
