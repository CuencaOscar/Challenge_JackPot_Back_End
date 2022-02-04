from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Fruit(models.Model):
    name = models.CharField(max_length=10)
    value = models.SmallIntegerField()
    img = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} --- {self.name} --- {self.value}"

class CreditUser(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    credit = models.SmallIntegerField(default=10)

    def __str__(self):
        return f"{self.user} --- {self.credit}"