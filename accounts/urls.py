from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('profile/',views.profile, name='profile'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogout, name='logout'),
]
