from django.shortcuts import render
from django.views.generic import TemplateView
from book_post.models import BookPosts
from categories.models import Category
# Create your views here.

# class HomeView(TemplateView):
#     template_name = 'index.html'

# def home(request, category_slug = None):
#     data = BookPosts.objects.all()
#     if category_slug is not None:
#         category = Category.objects.get(slug = category_slug)
#         data = BookPosts.objects.filter(category = category)
#     categories = BookPosts.objects.all()
#     return render(request, 'index.html' ,{'data':data, 'category':categories})

def home(request, category_slug = None):
    data = BookPosts.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = BookPosts.objects.filter(category  = category)
    categories = Category.objects.all()
    return render(request, 'index.html', {'data' : data, 'category' : categories})