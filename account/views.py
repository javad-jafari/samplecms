from django.contrib.auth import logout, authenticate, login, get_user_model,update_session_auth_hash
from django.contrib.auth.views import LoginView

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import RedirectView ,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from account.forms import RegisterForm

class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class SignView(LoginView):
    template_name = 'registrate/login.html'
    redirect_authenticated_user = '/'




class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        return render(request, 'registrate/register.html', {'form': RegisterForm})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()           
            return redirect('login')

        return render(request, 'registrate/register.html', {'form': form})
