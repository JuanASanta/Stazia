from django.contrib import admin
from .models import Tenant

# Register your models here.
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

admin.site.register(Tenant, TenantAdmin)