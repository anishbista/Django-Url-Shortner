from django.contrib import admin
from .models import ShortUrl


@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ["original_url", "short_url", "user"]
