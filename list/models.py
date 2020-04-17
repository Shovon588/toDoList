from django.db import models
from datetime import datetime

# Create your models here.


class UserIP(models.Model):
    ip = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.ip


class Item(models.Model):
    user = models.ForeignKey(UserIP, on_delete=models.CASCADE)

    item = models.CharField(max_length=1000)
    done = models.BooleanField(default=False)
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return "Ip: %s, Item: %s" %(self.user.ip, self.item)
