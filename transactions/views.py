from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Transaction
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Sum
from django.views import View
from accounts.models import UserAccounts
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .forms import DepositForm
# Create your views here.

def send_transaction_email(user, amount ,subject, template):
    message = render_to_string(template,{
        'user': user,
        'amount': amount
    })
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()
# Create your views here.
    
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/deposit.html'
    model = Transaction
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                'account' : self.request.user.account,
            }
        )
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title':self.title
        })
        return context

class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = ''
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields = ['balance']
        )
        send_transaction_email(self.request.user, amount, 'Deposit Message', 'transactions/deposit_email.html')
        messages.success(self.request, f'{amount}$ was deposit successfully')
        return super().form_valid(form)
    