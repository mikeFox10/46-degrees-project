from enum import unique
from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=30, unique=True)
    class Meta:
        ordering = ['user']
    def __str__(self):
        return "%s" % (self.user)

class Iou(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=30)	
    expiration = models.DateField()
    lender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lender')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrower')

    class Meta:
        ordering = ['amount']