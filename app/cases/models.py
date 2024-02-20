from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Wash(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=25)
    desc = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} (XCD${self.price})"


class Case(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="owners", null=True
    )
    photo = models.ImageField(upload_to="vehicles/photos", blank=True)
    plate = models.CharField(max_length=10)
    wash = models.ForeignKey(Wash, on_delete=models.PROTECT, related_name="wash_list")
    date = models.DateField()
    notes = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        if self.plate:
            return self.plate
        return f"{self.user} - {self.date}"
