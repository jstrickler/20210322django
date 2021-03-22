from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import DocForm

# Create your views here.

# example:
def home(request):
    context = { 'message': 'File Upload Demo' }
    return render(request, 'upload/home.html', context)

def simple_upload(request):
    context = { 'message': 'Uploading files' }

    if request.method == 'POST' and request.FILES['myfile']:
        # 'myfile' is button name on form
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload/simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload:home')
    else:
        form = DocForm()
    return render(request, 'upload/model_form_upload.html', {
        'form': form
    })
