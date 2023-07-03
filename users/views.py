from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomUserForm

from .models import *


class MyLoginView(LoginView):
    template_name = "users/login.html"
    form_class = CustomUserForm
    success_url = reverse_lazy('statistic_app:index')
    def get_success_url(self) -> str:
        return self.success_url



class MyRegisterView(CreateView):
    model = CustomUser
    template_name = "users/register.html"
    form_class = CustomUserForm
    success_url = reverse_lazy("users:login_page")
    success_msg = 'Пользователь создан'




def log_out(request):
    logout(request)
    return redirect(reverse("users:login_page"))


# from django.views.generic.edit import CreateView
# class CreateProfilePageView(CreateView):
#     model = Profile

#     template_name = 'base/create_profile.html'
#     fields = ['profile_pic', 'bio', 'facebook', 'twitter', 'instagram']
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

#     success_url = reverse_lazy('tasks')


