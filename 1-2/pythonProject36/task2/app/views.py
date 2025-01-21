from django.shortcuts import render, HttpResponse
from .models import Cat


# Create your views here.
def forms(request):
    if 'cat_name' in request.GET:
        cat_name = request.GET.get('cat_name')
        cats = [cat.cat_breed for cat in Cat.objects.filter(cat_name=cat_name)]
        return HttpResponse(f"{', '.join(cats)}")
    elif 'cat_breed' in request.GET:
        cat_breed = request.GET.get('cat_breed')
        cats = [cat.cat_name for cat in Cat.objects.filter(cat_breed=cat_breed)]
        return HttpResponse(f"{', '.join(cats)}")
    elif request.method == "POST":
        cat_name = request.POST.get('cat_name')
        cat_breed = request.POST.get('cat_breed')
        Cat.objects.create(cat_name=cat_name, cat_breed=cat_breed)
    return render(request, 'app/forms.html')