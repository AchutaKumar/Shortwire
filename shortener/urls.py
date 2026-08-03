from django.urls import path
from .views import ShortenView, RedirectView, StatsView, IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('api/shorten', ShortenView.as_view()),
    path('api/stats/<str:short_code>', StatsView.as_view()),
    path('<str:short_code>', RedirectView.as_view()),
]