from django.shortcuts import render
# from . models import People
from .models import Place
from .models import People


# Create your views here.

def demo(request):
    obj = Place.objects.all()
    return render(request, "index.html", {'result': obj})


def demo1(request):
    obj1 = People.objects.all()
    return render(request, "index.html", {'add': obj1})
