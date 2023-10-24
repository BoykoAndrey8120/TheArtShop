from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = 'home'


class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'
    # next_page = reverse_lazy('home')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически войдите в систему после регистрации
            return redirect('home')  # Замените 'home' на URL-маршрут вашей домашней страницы
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
