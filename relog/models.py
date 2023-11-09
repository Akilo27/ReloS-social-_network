from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    title = models.CharField(max_length=10)
    order_by = models.IntegerField(default=0)

    def __str__(self):
        return self.title



