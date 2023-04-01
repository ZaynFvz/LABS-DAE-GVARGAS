from django.shortcuts import render
import math
# Create your views here.
def index(request):
    context={
        'titulo':"CÁLCULO DEL VOLUMEN DE UN CILINDRO"
    }
    return render(request,'vcilindro/formulario.html',context)

def calcular(request):
    if request.method == 'POST':
        diametro=request.POST['diametro']
        altura=request.POST['altura']
        radio=float(diametro)/2
        pi=math.pi
        area_cilindro=pi*pow(radio,2)
        resultado=area_cilindro*float(altura)
    context={
        'titulo':"Tenemos el volumen",
        'diametro':request.POST['diametro'],
        'altura':request.POST['altura'],
        'resultado':resultado,
    }
    return render(request,'vcilindro/respuesta.html',context)
