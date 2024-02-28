from django.db import models
from django.contrib.auth.models import User
import string
import random


class ShortUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url

    def save(self, *args, **kwargs):
        self.short_url = self.generate_short_url()
        return super().save(*args, **kwargs)

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = "".join(random.choice(characters) for _ in range(6))
        return short_url
