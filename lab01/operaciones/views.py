from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Estas en la página de operaciones !!!</h1>")

def sumar(request, sum_n1,sum_n2):
    adicion = sum_n1+sum_n2
    return HttpResponse("<h1>La suma de %s + %s es %s</h1>" %(sum_n1,sum_n2,adicion)) 

def resta(request, res_n1,res_n2):
    diferencia = res_n1-res_n2
    return HttpResponse("<h1>El resultado de restar %s - %s es %s</h1>" %(res_n1,res_n2,diferencia))

def multiplicacion(request, pro_n1,pro_n2):
    producto = pro_n1*pro_n2
    return HttpResponse("<h1>El producto de %s x %s es %s</h1>" %(pro_n1,pro_n2,producto))
