from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car



def car_index(request):
    cars = Car.objects.all() 
    return render(request, 'cars/index.html', {'cars': cars})

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {'car': car})


class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'description']
    success_url = '/cars/'


class CarUpdate(UpdateView):
      model = Car
      fields = ['make', 'model', 'year', 'description']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'    