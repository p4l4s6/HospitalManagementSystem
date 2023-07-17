from django.db import models
from django.contrib.auth.models import AbstractUser

from authapp.constants import GenderChoice, RoleChoice


# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=20, unique=True)
    gender = models.IntegerField(choices=GenderChoice.choices)
    role = models.IntegerField(
        choices=RoleChoice.choices,
        default=RoleChoice.PATIENT
    )


class Slot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)
