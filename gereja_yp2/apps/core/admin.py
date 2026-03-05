from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from config.admin_site import admin_site

# Register built-in auth models with our custom admin site
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
