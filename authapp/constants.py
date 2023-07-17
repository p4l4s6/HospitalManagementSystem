from django.db import models


class RoleChoice(models.IntegerChoices):
    PATIENT = 0, "Patient"
    DOCTOR = 1, "Doctor"
    ASSISTANT = 2, "Assistant"


class GenderChoice(models.IntegerChoices):
    MAN = 0, "Man"
    WOMEN = 1, "Women"
