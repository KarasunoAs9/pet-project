from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>", views.ReveiwsPage.as_view(), name="reviews-page"),
]
