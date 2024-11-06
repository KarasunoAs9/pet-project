from django.contrib import admin
from .models import Cart, Orders, Payment
# Register your models here.

class OrdersAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


admin.site.register(Cart)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Payment)