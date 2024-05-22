from django.db import models


class Organization(models.Model):
    organization_name = models.CharField(max_length=200, unique=True)
    total_money = models.IntegerField(default=0)
    spend_money = models.PositiveBigIntegerField(default=0)
    current_money = models.PositiveBigIntegerField(default=0)
    monthly_money = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.organization_name