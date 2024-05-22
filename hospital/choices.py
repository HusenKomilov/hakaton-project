from django.db import models


class StatusChoice(models.TextChoices):
    IN_VIEW = "Ko'rikda", "Korikda"
    EMPTY = "Bo'sh", "Bo'sh"
    VACATION = "Dam olishda",  "Dam olishda"
