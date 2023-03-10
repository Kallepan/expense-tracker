from django.db import models

from authentication.models import User

class Payee(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self) -> str:
        return self.name

class Expense(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    payee = models.ForeignKey(to=Payee, on_delete=models.SET_NULL, null=True, blank=True)
    reason = models.TextField(max_length=500, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)