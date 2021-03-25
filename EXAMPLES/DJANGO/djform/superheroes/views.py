"""
    Views for the DJForms Project

    These are forms illustrating how forms work in Django
"""
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls import reverse  # get URL from view name
from .forms import DemoForm, HeroSearchForm, HeroAddForm
from .models import Superhero, City

def home(request):
    """
    Welcome page

    :param request: HTTP request
    :return: HTTP Response
    """
    data = {
        'message': 'Welcome to the superheroes app for forms',
    }
    return render(request, 'superheroes/home.html', data)


def demoform(request):
    """
    Generic form demo with various fields

    :param request: HTTP request
    :return: HTTP Response
    """
    invalid = False

    if request.method == 'POST':
        form = DemoForm(request.POST)
        if form.is_valid():
            # if data is valid, show results page
            # email = form.cleaned_data.get('demo_email')
            context = {
                    'page_title': 'Form Fields Results',
                    'data': form.cleaned_data,
            }
            return render(request, 'superheroes/form_results.html', context)
        else:
            # show form with errors for correcting
            invalid = True
    else:
        form = DemoForm() # unbound form

    # unless POST/valid, redraw form
    context = {
        'page_title': 'Form Fields Example',
        'form': form,
        'invalid': invalid,
    }
    return render(request, 'superheroes/form_demo.html', context)


def herosearch(request):
    """
    View a form with a name search blank for heros, and a color choice for the hero's name

    :param request: HTTP request
    :return: HTTP Response
    """
    # bound (filled-in) form
    if request.method == 'POST':
        form = HeroSearchForm(request.POST)
        if form.is_valid():
            hero_name = form.cleaned_data.get('hero_name')
            hero_color = form.cleaned_data.get('hero_color')
            # request.session['color'] = hero_color
            hero = get_object_or_404(Superhero, name=hero_name)
            context = {
                'page_title': 'Hero Details',
                'hero': hero,
                'color': hero_color,
            }
            return render(request, 'superheroes/hero_details.html', context)

    else:
        # unbound (empty) form
        form = HeroSearchForm()

        context = {
            'page_title': 'Hero Search',
            'form': form,
        }
        return render(request, 'superheroes/hero_select.html', context)

def success(request, hero_name):
    """
    View for success database addition.

    :param request:
    :param hero_name: name of hero (str)
    :return: HTTP response with success message
    """
    return render(request, 'superheroes/success.html', context={'hero_name': hero_name})

def heroadd(request):
    """
    View to provide form for adding one hero to the database

    :param request: HTTP request
    :return: HTTP Response
    """

    # bound (filled-in) form
    if request.method == 'POST':
        form = HeroAddForm(request.POST)
        if form.is_valid():
            hero = Superhero()
            hero.name = form.cleaned_data.get('name')
            hero.secret_identity = form.cleaned_data.get('secret_identity')
            hero.real_name = form.cleaned_data.get('real_name')
            city_id = form.data.get('city')
            hero.city = City.objects.get(pk=city_id)
            # get enemies and powers and add to enemies/powers DB if necessary
            # add enemies and powers to hero
            hero.save() # executes SQL code to add hero to DB
            context = {
                'page_title': 'Hero Added',
                'hero': hero,
                'added': True,
            }
            return redirect(reverse('superheroes:success', kwargs={'hero_name': hero.name}))
        else:
            return HttpResponse("Well that ended well")

    else:
        # unbound (empty) form
        form = HeroAddForm()

        context = {
            'page_title': 'Form Example',
            'form': form,
        }
        return render(request, 'superheroes/hero_add.html', context)

