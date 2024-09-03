from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from .forms import ServiceForm


def add_service(request, car_id):

    form = ServiceForm(request.POST)
    if form.is_valid():
        
        new_Service = form.save(commit=False)
        new_Service.car_id = car_id
        new_Service.save()
    return redirect('car-detail', car_id=car_id)


def car_index(request):
    cars = Car.objects.all() 
    return render(request, 'cars/index.html', {'cars': cars})

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    service_form = ServiceForm()
    # print(car)
    return render(request, 'cars/detail.html', {
        'car': car, 'service_form': service_form
        })


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