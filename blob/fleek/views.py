from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render

# Create your views here.



# example without template (only used in class -- always use templates in real life):
def home(request):
    return HttpResponse("Welcome to fleek. Are we having fun yet?")

# example with template (normal Django approach)
# def home(request):
#     context = { 'message': "Welcome to fleek" }
#     return render(request, 'fleek/home.html', context)

def vogg(request):
    return HttpResponse("This is the VOGG page")

def blenn(request):
    return HttpResponse("This is the BLENN page")
