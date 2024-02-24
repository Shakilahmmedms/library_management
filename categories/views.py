from django.shortcuts import render
from .import models
# Create your views here.
def add_category(request):
    category = models.Category.objects.all()
    return render(request, 'index.html', {'category':category})
    