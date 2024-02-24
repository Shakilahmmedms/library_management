from django.shortcuts import render, redirect
from django.views.generic import FormView,CreateView
from .forms import UserSignupForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from book_post.models import BookPosts,BuyNow
# Create your views here.
class UserSignupView(FormView):
    template_name = 'accounts/user_signup.html'
    form_class = UserSignupForm
    success_url = reverse_lazy('signup')

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        print(user)
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Login successfully. Welcome Back !')
        return super().form_valid(form)
    

def UserLogout(request):
    logout(request)
    messages.info(request, 'Logout successfully.!')
    return redirect('home')

@login_required
def profile(request):
    books = BookPosts.objects.all()
    buy_history = BuyNow.objects.filter(user=request.user)
    return render(request,'accounts/profile.html', {'buy_history':buy_history,'books':books})

