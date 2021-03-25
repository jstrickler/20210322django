from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse
from .models import Dog, Breed
from .forms import DogAddForm, OtherForm
from django.db.models import Q
import pdb

# Create your views here.
def home(request):
    dogs = Dog.objects.all()
    context = {
        'page_title': 'Welcome to the Dogs',
        'dogs': dogs,
        'home': True,
    }
    return render(request, 'dogs_core/home.html', context)

def dog_details(request, pkid):
    dog = get_object_or_404(Dog, pk=pkid)
    return render(request, 'dogs_core/dog_details.html', {'dog': dog})

def dog_add(request):
    if request.method == 'POST':
        form = DogAddForm(request.POST)  # fill in form with user data
        if form.is_valid():
            dog = Dog()
            dog.name = form.cleaned_data.get('name')
            breed_id = form.data.get('breed')
            dog.breed = Breed.objects.get(pk=breed_id)
            dog.sex = form.cleaned_data.get('sex')
            dog.is_neutered = form.cleaned_data.get('is_neutered')
            dog.save()  # add to DB

            context = {
                'page_title': f"Added {dog.name}",
                'dog': dog,
                'added': True,
            }
            return render(request, 'dogs_core/dog_details.html', context)
    else:
        form = DogAddForm()
        context = {
            'page title': 'Add a Dog',
            'form': form,
        }
        return render(request, 'dogs_core/dog_add.html', context)

def other_form(request):
    if request.method == 'POST':  # filled out form
        form = OtherForm(request.POST)  # fill in form from incoming data
        if form.is_valid():
            dog_name = form.cleaned_data.get('dog_name')
            query = Q()
            if dog_name:
                query &= Q(dog_name=dog_name)
            dog_sex = form.cleaned_data.get('dog_sex')
            if dog_sex:
                query &= Q(dog_sex=dog_sex)
            results = Dog.objects.filter(query)

    else:  # empty form
        form = OtherForm()
        context = {
        'page title': 'Other Form',
        'form': form,
        }
        return render(request, 'dogs_core/other_form.html', context)

# example without template (only used in class -- always use templates in real life):
# def home(request):
#     return HttpResponse("Welcome to dogs_core")

# example with template (normal Django approach)
# def home(request):
#     context = { 'message': "Welcome to dogs_core" }
#     return render(request, 'dogs_core/home.html', context)
class DogListView(ListView):
    model = Dog   # template will be dog_list.html by default
    # template_name = "dogs_core/whatever.html"

class DogListByNameView(ListView):
    model = Dog   # template will be dog_list.html by default
    template_name = "dogs_core/dog_list_by_name.html"

class DogDetailView(DetailView):
    model = Dog  # template will be dog_detail.html

class DogDetailByNameView(DetailView):
    model = Dog  # template will be dog_detail.html

    def get_object(self, queryset=None):
        return Dog.objects.get(name=self.kwargs.get("name"))

class BreedListView(ListView):
    model = Breed

class BreedDetailView(DetailView):
    model = Breed