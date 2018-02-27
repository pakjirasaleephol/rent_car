from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Car,Rent
from .models import Person
from .forms import PersonForm
from .forms import CarForm
from .forms import RentForm


def home(request):
	return render(request, 'home.html')
	
class CreatePersonView(CreateView):
	queryset = Person()
	template_name='create_person.html'
	form_class = PersonForm
	success_url = '/personlist'

class CreateCarView(CreateView):
	queryset = Car()
	template_name='create_car.html'
	form_class = CarForm
	success_url = '/admin'

# use this
class CreateRentView(CreateView): 
	queryset = Rent()
	template_name='rent_car.html'
	form_class = RentForm
	success_url = '/admin'

class ListPersonView(ListView): 
    model = Person
    template_name='person_list.html'
    form_class = PersonForm
    success_url = '/admin'

# use this
class CarListView(ListView):
    model = Car
    template_name='car_list.html'

class RentListView(ListView):
    model = Rent
    template_name='rent_list.html'
    form_class = RentForm

