from django.db import models
from django.contrib.auth.models import AbstractUser
from tenant.models import Tenant

# Create your models here.
class User(AbstractUser):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='users')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=9, min_length=9, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.full_name + " (" + self.email + ")"