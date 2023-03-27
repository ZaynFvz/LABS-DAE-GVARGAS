from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Desde la vista de encuestas!!!</h1>")

def detalle(request, pregunta_id):
    return HttpResponse("<h1>Estas viendo la pregunta %s.</h1>" % pregunta_id)

def resultados(request, pregunta_id):
    response = "<h1>Estas viendo los resultado de la pregunta %s.</h1>"
    return HttpResponse(response % pregunta_id)

def votar(request, pregunta_id):
    return HttpResponse("<h1>Estas votando por la pregunta %s.</h1>" % pregunta_id)

