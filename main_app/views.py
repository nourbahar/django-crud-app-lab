from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Car
from .forms import ServiceForm

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
   

def add_service(request, car_id):

    form = ServiceForm(request.POST)
    if form.is_valid():
        
        new_Service = form.save(commit=False)
        new_Service.car_id = car_id
        new_Service.save()
    return redirect('car-detail', car_id=car_id)

@login_required
def car_index(request):
    cars = Car.objects.filter(user=request.user) 
    return render(request, 'cars/index.html', {'cars': cars})

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    service_form = ServiceForm()
    # print(car)
    return render(request, 'cars/detail.html', {
        'car': car, 'service_form': service_form
        })

class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/cars/'


class CarUpdate(UpdateView):
      model = Car
      fields = ['make', 'model', 'year', 'description']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'    