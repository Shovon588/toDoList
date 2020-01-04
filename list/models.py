from django.db import models
from datetime import datetime

# Create your models here.


class Item(models.Model):
    item = models.CharField(max_length=1000)
    done = models.BooleanField(default=False)
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.item
