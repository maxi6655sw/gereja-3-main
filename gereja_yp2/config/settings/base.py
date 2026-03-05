"""
Base Django settings for gereja_yp2 project.
Shared across all environments.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR points to the project root (where manage.py lives)
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Application definition

INSTALLED_APPS = [
    # Jazzmin must come BEFORE django.contrib.admin
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local apps
    'apps.core',
    'apps.berita',
    'apps.jadwal',
]


# ---------------------------------------------------------------------------
# Jazzmin — Modern Admin UI
# Docs: https://django-jazzmin.readthedocs.io/configuration/
# ---------------------------------------------------------------------------
JAZZMIN_SETTINGS = {
    # ── Branding ────────────────────────────────────────────────────────────
    "site_title": "Admin Gereja YP2",
    "site_header": "Gereja Santo Yohanes Paulus II",
    "site_brand": "Gereja YP2",
    "site_logo": "img/logo-Yp.png",         # relative to STATIC
    "site_logo_classes": "img-circle",
    "site_icon": "img/logo-Yp.png",
    "welcome_sign": "Selamat Datang, Admin",
    "copyright": "Gereja St. Yohanes Paulus II © 2024",

    # ── Top-bar search ───────────────────────────────────────────────────────
    "search_model": ["berita.Berita", "auth.User"],

    # ── User menu (top-right) ────────────────────────────────────────────────
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Beranda Website", "url": "/", "new_window": True, "icon": "fas fa-globe"},
    ],

    # ── Sidebar navigation ───────────────────────────────────────────────────
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": [
        "berita", "berita.Berita", "berita.Kategori",
        "jadwal", "jadwal.JadwalMisa",
        "auth",
    ],
    "icons": {
        "auth":                  "fas fa-users-cog",
        "auth.user":             "fas fa-user",
        "auth.Group":            "fas fa-users",
        "berita.Berita":         "fas fa-newspaper",
        "berita.Kategori":       "fas fa-tags",
        "jadwal.JadwalMisa":     "fas fa-calendar-alt",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # ── Related-modal pop-ups ─────────────────────────────────────────────────
    "related_modal_active": True,

    # ── Sidebar quick-add links ─────────────────────────────────────────
    "custom_links": {
        "berita": [
            {
                "name":  "+ Tambah Berita",
                "url":   "custom_admin:berita_berita_add",
                "icon":  "fas fa-plus-circle",
                "permissions": ["berita.add_berita"],
            },
            {
                "name":  "+ Tambah Kategori",
                "url":   "custom_admin:berita_kategori_add",
                "icon":  "fas fa-folder-plus",
                "permissions": ["berita.add_kategori"],
            },
        ],
        "jadwal": [
            {
                "name":  "+ Tambah Jadwal",
                "url":   "custom_admin:jadwal_jadwalmisa_add",
                "icon":  "fas fa-calendar-plus",
                "permissions": ["jadwal.add_jadwalmisa"],
            },
        ],
    },

    # ── UI Tweaks ───────────────────────────────────────────────────
    "custom_css": "css/admin_custom.css",
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,    # set True temporarily to play with themes

    # ── Change-form ───────────────────────────────────────────────────────────
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user":  "collapsible",
        "auth.group": "vertical_tabs",
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour":          "navbar-primary",
    "accent":                "accent-primary",
    "navbar":                "navbar-dark",
    "no_navbar_border":      False,
    "navbar_fixed":          True,
    "layout_boxed":          False,
    "footer_fixed":          False,
    "sidebar_fixed":         True,
    "sidebar":               "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme":                 "default",
    "default_theme_mode":    "light",
    "button_classes": {
        "primary":   "btn-primary",
        "secondary": "btn-secondary",
        "info":      "btn-info",
        "warning":   "btn-warning",
        "danger":    "btn-danger",
        "success":   "btn-success",
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (User uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth
LOGIN_REDIRECT_URL = '/admin/'
