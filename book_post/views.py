from django.shortcuts import render,redirect,get_object_or_404
from .import forms
from .import models
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages
from transactions.views import send_transaction_email
from transactions.models import Transaction
from django.utils import timezone
from django.views.generic import DeleteView
def detail_post_view(request, id):
    books = models.BookPosts.objects.get(id=id)
    
    if request.method == 'POST':
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.books = books
            new_comment.save()
    
    comments = books.comments.all()
    comment_form = forms.CommentForm()
    
    context = {
        'books': books,
        'comments': comments,
        'comment_form': comment_form
    }
    
    return render(request, 'book_details.html', context)


@login_required
def buy_book(request, id):
    book = models.BookPosts.objects.get(id=id)
    books = models.BookPosts.objects.all()
    if book.quantity > 0:
        book_cost = book.price
        user_balance = request.user.account.balance
        if user_balance >= book_cost:
            user_account = request.user.account
            models.BuyNow.objects.create(user=request.user, book=book)
            book.quantity -= 1
            user_account.balance -= book_cost
            user_account.save()
            book.save()
            messages.success(request, 'Book Buy Successfully')
            send_transaction_email(request.user, book.price, 'Book Buy', 'buy_book_email.html')
            return render(request, './accounts/profile.html',{'books':books})
        else:
             messages.error(request, 'Your do not have enough balance')
    else:
        messages.error(request, 'Book is out of stock')
    
    return render(request, './accounts/profile.html',{'books':books})


class ReturnBookView(DeleteView):
    model = models.BookPosts
    template_name = 'accounts/profile.html' 
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

    def delete(self, request, *args, **kwargs):

        book = models.BookPosts.objects.get(id=id)
        book_cost = book.price
        user_account = request.user.account
        models.BuyNow.objects.create(user=request.user, book=book)
        book.quantity += 1
        user_account.balance += book_cost
        user_account.save()
        book.save()
        messages.success(request, f'Book {book.title} returned successfully. Your balance has been updated.')
        return super().delete(request, *args, **kwargs)

