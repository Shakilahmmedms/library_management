from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserAccounts
# Create your models here.

class Transaction(models.Model):
    account = models.ForeignKey(UserAccounts, related_name = 'transactions', on_delete= models.CASCADE)
    amount = models.DecimalField(max_digits = 12, decimal_places = 2)
    balance_after_transaction = models.DecimalField(max_digits = 12, decimal_places = 2)
