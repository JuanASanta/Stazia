from django.db import models
from tenant.models import Tenant

# Create your models here.
class Property(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name + " - " + self.address