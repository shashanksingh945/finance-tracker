from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    date=models.DateField()
    description=models.TextField()

    def __str__(self):
        return f"{self.ammount}-{self.category}"