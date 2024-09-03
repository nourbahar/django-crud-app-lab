from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

SERVICE_TYPES = (
    ('O', 'Oil Change'),
    ('T', 'Tire Rotation'),
    ('B', 'Brake Repair'),
    ('E', 'Engine turn-up'),
    ('W', 'Wheel Alignment'),
    ('A', 'Air Conditioning  Service'),
    ('D', 'Detailing'),
    ('S', 'Suspension Repair'),
)



class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})
    
    


class Service(models.Model):
    date = models.DateField('Service date')
    service_type = models.CharField(
        max_length=1,
        choices=SERVICE_TYPES,
        default=SERVICE_TYPES[0][0]
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_service_type_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
