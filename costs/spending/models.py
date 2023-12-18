from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    
class Spending(models.Model):
    price = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spendings')
    category = models.CharField(max_length=75, default=None)
    timestamp = models.DateField(auto_now_add=True)