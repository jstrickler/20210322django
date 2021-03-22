import csv

from django.shortcuts import render
from django.http import HttpResponse
from superheroes.models import Superhero, City
from reportlab.pdfgen import canvas

def home(request):
    context = { 'message': 'Hello' }
    return render(request, 'export/home.html', context)


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="superheroes.csv"'

    writer = csv.writer(response)
    for hero in Superhero.objects.all():
        writer.writerow([hero.name, hero.secret_identity, hero.city])

    return response


def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="superheroes.pdf"'

    pdf = canvas.Canvas(response)

    y_pos = 800
    x_pos = 100
    for hero in Superhero.objects.all():
        pdf.drawString(x_pos, y_pos, hero.name)
        pdf.drawString(x_pos+100, y_pos, hero.secret_identity)
        pdf.drawString(x_pos+200, y_pos, hero.city.name)
        y_pos -= 15

    pdf.showPage()
    pdf.save()

    return response
