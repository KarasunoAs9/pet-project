from django.urls import path
from . import views

urlpatterns = [
    path("cart/", views.CartView.as_view(), name="cart-page"),
    path("cart/delete", views.DeleteProduct.as_view(), name="delete-product"),
    path("cart/update", views.UpdateQuantity.as_view(), name="update-cart")
]
