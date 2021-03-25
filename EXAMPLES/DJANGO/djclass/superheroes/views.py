from django.views.generic import (
    TemplateView, ListView, CreateView, DetailView, UpdateView
)
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Superhero, City

class WombatView(TemplateView):
    template_name = "superheroes/wombat.html"

class SharedDataTemplateView(TemplateView):
    data = {
        'color': 'green',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.data)  # add self.data dict to existing dict in template
        return context

class HomeView(SharedDataTemplateView):
    template_name = 'superheroes/home.html'
    data = {
        'message': 'Welcome to the superheroes app for class-based views',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.data)  # add self.data dict to existing dict in template
        return context

class HeroListViewMinimal(ListView):
    model = Superhero

class HeroDetailViewMinimal(DetailView):
    model = Superhero

class HeroListView(ListView):
    context_object_name = 'heroes'
    model = Superhero

class HeroDetailView(DetailView):
    context_object_name = 'hero'
    model = Superhero

class HeroCreateView(CreateView):
    model = Superhero
    fields = ['name', 'real_name', 'secret_identity', 'city']
    success_url = reverse_lazy('superheroes:success')

class CityCreateView(CreateView):
    model = City
    fields = ['name']
    success_url = reverse_lazy('superheroes:success')

class HeroUpdateView(UpdateView):
    model = Superhero
    # template = "hero_update.html"
    fields = ['name', 'real_name', 'secret_identity', 'city']
    success_url = reverse_lazy('superheroes:success')

class SuccessView(TemplateView):
    template_name = 'superheroes/success.html'
