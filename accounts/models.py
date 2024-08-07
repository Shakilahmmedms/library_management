from django.db import models
from django.contrib.auth.models import User
from book_post.models import BookPosts, BuyNow

# Create your models here.


    
class UserAccounts(models.Model):
    user = models.OneToOneField(User, related_name ='account', on_delete = models.CASCADE)
    account_no = models.IntegerField(unique = True)
    initial_deposit_date = models.DateField(auto_now_add = True)
    balance = models.DecimalField(default = 0,max_digits =12,decimal_places = 2)
    buy_history = models.ManyToManyField(BuyNow)

    def __str__(self):
        return str(self.account_no)
    


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     buy_history = models.ManyToManyField(BuyNow)

