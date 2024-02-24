from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class BookPosts(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    content= models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/', blank=True, null= True)
    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    books = models.ForeignKey(BookPosts, on_delete= models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length= 50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f'Comment by{self.name}'
    

class BuyNow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookPosts, on_delete=models.CASCADE)
    buy_date = models.DateTimeField(auto_now_add=True)