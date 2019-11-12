from django.contrib import admin
from .models import UrlObject


@admin.register(UrlObject)
class PlatformAdmin(admin.ModelAdmin):
    pass
