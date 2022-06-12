from django.contrib import admin
from .models import Payment


# admin.site.register(Dues)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user','amount', 'date_created')
    search_fields = ('user',)
