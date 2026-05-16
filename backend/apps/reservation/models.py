from django.db import models
from apps.property.models import Property
from django.core.exceptions import ValidationError


# Create your models here.
class Reservation(models.Model):
    STATE_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
    ]

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    state = models.CharField(choices=STATE_CHOICES)
    guests = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reservation for {self.property.name} from {self.start_date} to {self.end_date}"
    
    def clean(self):
        """
        Comprobar que la fecha de inicio es anterior a la fecha de fin
        """
        if self.start_date >= self.end_date:
            raise ValidationError("La fecha de inicio debe ser anterior a la fecha de fin.")
        
    def save(self, *args, **kwargs):
        self.clean()  # Llamar al método clean para validar antes de guardar
        super().save(*args, **kwargs)  # Llamar al método save original para guardar el objeto
    
