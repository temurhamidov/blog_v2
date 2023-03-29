from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .models import User

from .forms import LoginForm, SignUpForm, ProfileUpdateForm


# Create your views here.

class LoginView(View):
    template_name = 'registration/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(self.request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('myapp:home')
        messages = 'Username or password invalid'
        context = {
            'form' : form,
            'messages' : messages,
        }
        return render(request, self.template_name, context)


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('user:login_view')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        context = {
            'user' : user
        }
        return render(request, 'registration/profile.html', context)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    form_class = ProfileUpdateForm
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('user:profile_view')


class PasswordChangeView(View):
    def get(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user)
        context = {
            'form' : form,
            'messages': 'Xatolik bor'
        }
        return render(request, 'registration/change_password.html', context)

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('user:profile_view')
        context = {
            'form': form,
            'messages' : 'Xatolik bor'
        }
        return render(request, 'registration/change_password.html', context)






