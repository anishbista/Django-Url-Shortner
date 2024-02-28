from django.urls import path
from .views import DashboardView, ShortUrlView

urlpatterns = [
    path("shorten/", ShortUrlView.as_view(), name="short_url"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
