from django.contrib import admin
from .models import BookPosts,Comment,BuyNow
# Register your models here.
admin.site.register(BookPosts)
admin.site.register(Comment)
admin.site.register(BuyNow)
