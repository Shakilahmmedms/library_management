from django import forms
from accounts.models import UserAccounts
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
   
    def save(self, commit = True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()
    

class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposti_amount = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_deposti_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposti_amount} $'
            )
        return amount
    