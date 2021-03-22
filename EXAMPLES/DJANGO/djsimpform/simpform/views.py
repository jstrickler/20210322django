from django.shortcuts import render
from .forms import SimpleForm

def home(request):
    if request.method == "POST":
        simpleform = SimpleForm(request.POST)
        if simpleform.is_valid():
            user_name = simpleform.cleaned_data["user_name"]
    else:
        user_name = ''
        simpleform = SimpleForm()

    context = {
        'message': "Welcome to Simple Form Demo App",
        'simpleform': simpleform,
        'username': user_name,
    }
    return render(request, 'simpform/home.html', context)
