from django.shortcuts import render, redirect
from .models import Car, Mod
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ServiceForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
def about(request):
  return render(request, 'about.html')

@login_required
def car_index(request):
  cars = Car.objects.filter(user=request.user)
  return render(request, 'cars/index.html', { 'cars': cars })

class Home(LoginView):
  template_name = 'home.html'

@login_required
def car_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  mods_car_doesnt_have = Mod.objects.exclude(id__in = car.mods.all().values_list('id'))
  service_form = ServiceForm()
  return render(request, 'cars/detail.html', {
    'car': car, 'service_form': service_form, 'mods': mods_car_doesnt_have
  })

@login_required
def add_service(request, car_id):
  form = ServiceForm(request.POST)
  if form.is_valid():
    new_service = form.save(commit=False)
    new_service.car_id = car_id
    new_service.save()
  return redirect('car-detail', car_id=car_id)

class CarCreate(CreateView):
  model = Car
  fields = 'model', 'year', 'description'
  success_url = '/cars'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
  model = Car
  fields = ['year', 'description']

class CarDelete(LoginRequiredMixin, DeleteView):
  model = Car
  success_url = '/cars/'

class ModCreate(LoginRequiredMixin, CreateView):
  model = Mod
  fields = '__all__'

class ModList(LoginRequiredMixin, ListView):
  model = Mod

class ModDetail(LoginRequiredMixin, DetailView):
  model = Mod

class ModUpdate(LoginRequiredMixin, UpdateView):
  model = Mod
  fields = ['name', 'color']

class ModDelete(LoginRequiredMixin, DeleteView):
  model = Mod
  success_url = '/mods/'

@login_required
def assoc_mod(request, car_id, mod_id):
  # Note that you can pass a toy's id instead of the whole object
  Car.objects.get(id=car_id).mods.add(mod_id)
  return redirect('car-detail', car_id=car_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('car-index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})