from django.shortcuts import render

def home(request):
    context = { 'message': "Let's do some Angular.JS" }
    return render(request, 'dogs/home.html', context)
