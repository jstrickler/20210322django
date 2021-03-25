from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Superhero

def home(request):
    return HttpResponse("Welcome to the superhero app")

def hero(request, hero_name):
    request.session['name'] = hero_name
    s = Superhero.objects.get(name=hero_name)
    return HttpResponse(
        "{} is really {}".format(s.secret_identity, s.name)
    )

def hero_by_id(request, pk):
    hero_name = request.session.get('name', '')
#    s = Superhero.objects.get(id=pk)
    s = get_object_or_404(Superhero, id=pk)  # automagically uses 404xx.html template
    return HttpResponse(
        "{} ({})".format(s.name, s.secret_identity)
    )