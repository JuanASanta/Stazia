from django.contrib import admin
from .models import Reservation

# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('property', 'start_date', 'end_date', 'customer_name', 'customer_email')
    search_fields = ('property__name', 'customer_name', 'customer_email')

admin.site.register(Reservation, ReservationAdmin)
