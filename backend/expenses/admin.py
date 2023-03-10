from django.contrib import admin

from .models import Payee, Expense

admin.site.register(Payee)
admin.site.register(Expense)