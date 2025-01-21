from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def log(request):
    if 'login-button' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)  # проверка логина, пароля

        if user is not None:
            login(request, user)
            return redirect(profile)
        else:
            return redirect(register)

    elif 'registration-button' in request.POST:
        return redirect(register)

    return render(request, "app/login.html")


def register(request): # Создание пользователя
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Имя занято')
        else:
            User.objects.create_user(username=username, password=password)
            return redirect(profile)
    return render(request, "app/registration.html")


@login_required
def profile(request):
    if 'new-name' in request.POST:# Изменение данных
        new_name = request.POST.get('new-name')
        if User.objects.filter(username=new_name).exists():
            pass
        else:
            User.objects.filter(id=request.user.id).update(username=new_name)
            return redirect(profile)
    elif request.method == "POST":# Удаление аккаунта
        request.user.delete()
        return redirect(log)

    return render(request, "app/profile.html", {'username': request.user.username})