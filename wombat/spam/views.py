from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<html><body><h1>Hello to Germany, England, and Hawaii (also NC)</h1></body></html>")

def sandwich(request):
    return HttpResponse("SPAM sandwich!")

