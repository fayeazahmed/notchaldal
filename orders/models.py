from django.db import models
from users.models import User
import datetime
# Create your models here.


class Order(models.Model):
    TIMING_CHOICES = [
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateField(default=datetime.date.today)
    preferred_time = models.CharField(choices=TIMING_CHOICES, max_length=20)
    total = models.PositiveIntegerField()
    comments = models.TextField(blank=True, null=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.email
