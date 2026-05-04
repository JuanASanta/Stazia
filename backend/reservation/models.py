from django.db import models
from property.models import Property

# Create your models here.
class Reservation(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    
    def __str__(self):
        return f"Reservation for {self.property.name} from {self.start_date} to {self.end_date}"