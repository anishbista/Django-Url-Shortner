from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ShortUrl


class ShortUrlView(LoginRequiredMixin, View):
    def post(self, request):
        original_url = request.POST.get("original_url")
        user = request.user
        short_url = ShortUrl.objects.create(user=user, original_url=original_url)
        return redirect("dashboard")

    def get(self, request):
        return render(request, "short_url.html")


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        short_urls = ShortUrl.objects.filter(user=request.user)
        context = {
            "short_urls": short_urls,
            "root_url": request.build_absolute_uri("/"),
        }
        return render(request, "dashboard.html", context)
