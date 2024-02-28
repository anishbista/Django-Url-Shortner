from django.urls import path
from .views import DashboardView, ShortUrlView, RedirectOriginalURLVIew

urlpatterns = [
    path("shorten/", ShortUrlView.as_view(), name="shorten"),
    path("", DashboardView.as_view(), name="dashboard"),
    path(
        "<str:short_url>/",
        RedirectOriginalURLVIew.as_view(),
        name="redirect_to_original_url",
    ),
]
