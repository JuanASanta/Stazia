from django.db import models
from apps.tenant.models import Tenant

# Create your models here.
class Property(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='properties')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name + " - " + self.address