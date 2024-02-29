from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ShortUrl
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages


class ShortUrlView(LoginRequiredMixin, View):
    def post(self, request):
        original_url = request.POST.get("original_url")
        user = request.user
        existing_url = ShortUrl.objects.filter(original_url=original_url).first()
        if existing_url:
            short_url = request.build_absolute_uri("/") + existing_url.short_url
            messages.error(
                request,
                f"URL already exists. It is {short_url}",
            )
        else:
            short_url = ShortUrl.objects.create(user=user, original_url=original_url)
        return redirect("dashboard")

    def get(self, request):
        return render(request, "main/shorten_url.html")


class DashboardView(LoginRequiredMixin, View):
    def post(self, request):

        return redirect("dashboard")

    def get(self, request):
        short_urls = ShortUrl.objects.all()
        context = {
            "short_urls": short_urls,
            "root_url": request.build_absolute_uri("/"),
        }
        return render(request, "main/dashboard.html", context)


class RedirectOriginalURLVIew(View):
    def get(self, request, short_url):
        shortened_url = get_object_or_404(ShortUrl, short_url=short_url)
        return redirect(shortened_url.original_url)
