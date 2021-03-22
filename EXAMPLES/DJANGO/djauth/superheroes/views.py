from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import django.contrib.auth
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Superhero
from .forms import LoginForm

def home(request):
    request.session['color'] = 'red'
    request.session['city'] = 'Baltimore'

    return HttpResponse("Welcome to my SuperHero App!!! Bam!!")

def session1(request):
    request.session['animal'] ='wombat'
    return HttpResponse("Set session variable")

def session2(request):
    animal = request.session['animal']
    data = {
        'animal': animal,
        'session': request.session,
    }
    return render(request, 'sessioninfo.html', data)

@login_required
def hero(request, hero_name):
    color = request.session['color']

    s = get_object_or_404(Superhero, name=hero_name)
    powers = [p.name for p in s.powers]
    return HttpResponse(
        "{} is really {}".format(s.secret_identity, s.name
                                 )
    )


def login(request, next=''):
    if (request.method == 'POST'):
        # User submitted form; process to log them in

        # Get form
        form = LoginForm(request.POST)

        # Start context
        context = {}
        if (form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = django.contrib.auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:  # Only allow active users to log in
                # Successfully logged in
                django.contrib.auth.login(request, user)
                context['result'] = True

                # Are we told to redirect?
                next_page = request.POST.get('next', '')
                if (next_page):
                    return HttpResponseRedirect(next_page)
            else:
                # Some kind of failure
                context['result'] = False
        else:
            # Invalid form, give it back to them
            context['form'] = form
            context['invalid_form'] = True
    else:
        # See if already logged in
        try:
            next_page = request.GET['next']
            if request.user.is_authenticated:
                return HttpResponseRedirect(next_page)
        except:
            # Oh well
            pass

        # Just show the form
        context = {
            'form': LoginForm(),
        }

    return render(request, 'login.html', context)


def logout(request):
    django.contrib.auth.logout(request)

    return HttpResponseRedirect('/')
