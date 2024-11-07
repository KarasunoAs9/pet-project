from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>", views.base, name="reviews-page")
]
