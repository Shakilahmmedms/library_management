from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAccounts


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2' , 'first_name', 'last_name', 'email']
    
    def save(self, commit = True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()

            UserAccounts.objects.create(
                user = our_user,
                account_no = 100000 + our_user.id
            )
        return our_user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                 'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })