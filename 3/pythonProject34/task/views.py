from django.shortcuts import render, redirect, HttpResponse
from .models import Person
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


def forms(request):
    return render(request, 'task/forms.html')


@csrf_exempt
def room(request):
    if request.method == "POST":
        new_name = request.POST.get("new-name")
        Person.objects.create(name=new_name)
        return redirect(forms)

    if request.method == "GET":
        name = request.GET.get("name")
        if Person.objects.filter(name=name).exists():
            messages.error(request, 'Это имя занято')
        else:
            messages.success(request, 'Это имя свободно')
    return render(request, 'task/forms.html')


