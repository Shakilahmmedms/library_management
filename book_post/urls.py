from django.urls import path
from .import views
urlpatterns = [
    path('details/<int:id>',views.detail_post_view, name='book_details'),
    # path('buy/<int:id>/', views.buy_book, name='buy_book'),
    path('buy/<int:id>/', views.buy_book, name='buy_book'),
    path('return/<int:id>', views.ReturnBookView.as_view(), name='return_book'),

]