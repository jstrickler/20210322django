from django.shortcuts import render
from django.utils.translation import ugettext as _
from superheroes.models import Superhero

def home(request):
    superheroes = Superhero.objects.all()

    context = { 'message': _('Superheroes'), "superheroes": superheroes }

    return render(request, 'core/home.html', context)
