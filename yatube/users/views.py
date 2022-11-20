from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import CreationForm

from django.views.generic import CreateView

from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetConfirmView

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:change_password_done')


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_change_done.html'


class MyPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/users/password_reset_complete.html'


class MyPasswordResetEmailDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_email_done.html'
