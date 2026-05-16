from django.db import models
from apps.property.models import Property
from apps.tenant.models import Tenant
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

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='reservations')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reservations')
    start_date = models.DateField()
    end_date = models.DateField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='pending')
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
        
        # Buscar reservas solapadas
        overlapping_reservations = Reservation.objects.filter(
            property=self.property,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        )

        # Excluir esta reserva si estamos editando
        if self.pk:
            overlapping_reservations = overlapping_reservations.exclude(pk=self.pk)

        # Lanzar error si existe conflicto
        if overlapping_reservations.exists():
            raise ValidationError(
                "Ya existe una reserva para esas fechas."
            )
        
    def save(self, *args, **kwargs):
        self.full_clean()  # Llamar al método clean para validar antes de guardar
        super().save(*args, **kwargs)  # Llamar al método save original para guardar el objeto

    class Meta:
        indexes = [
            models.Index(fields=['tenant']),
            models.Index(fields=['property']),
            models.Index(fields=['start_date']),
            models.Index(fields=['state']),
        ]
    
