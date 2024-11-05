from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.MainPage.as_view(), name="main-page"),
    path("<slug:slug>", views.ProductPage.as_view(), name="product-page"),
    path("shop/", views.ShopPage.as_view(), name="shop-page"),
    path("shop/<slug:slug>", views.CategoryPage.as_view(), name="category-page"),
    path("add-to-cart/", views.AddToCart.as_view(), name="add-to-cart")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
