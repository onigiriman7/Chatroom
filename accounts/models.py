from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, default = '')
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.IntegerField(default = 0 )

    def __str__(self):
            return self.user.username
