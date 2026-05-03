from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from tenant.models import Tenant


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, tenant=None, phone=None, password=None):
        """
        Crea y guarda un usuario con el email, el tenant, el teléfono y la contraseña.
        """
        if not email:
            raise ValueError('El usuario debe tener un email')

        user = self.model(
            email=self.normalize_email(email),
            tenant=tenant,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        """
        Crea y guarda un superusuario con el email y la contraseña.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE, related_name='user', blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=9, blank=True, null=True)
    username = None

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email