from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'titulo': "Matemática Básica",
    }
    return render(request,'operaciones/formulario.html',context)

def resolver(request):
    
    if request.method=='POST':
        numero1=request.POST['numero1']
        numero2=request.POST['numero2']
        oprc=request.POST['oprc']
        if oprc=='suma':
            total=int(numero1)+int(numero2)
        elif oprc=='resta':
            total=int(numero1)-int(numero2)
        elif oprc=='multiplicacion':
            total=int(numero1)*int(numero2)
    
    context={
        'titulo': "Resultado de su operación",
        'numero1': request.POST['numero1'],
        'numero2': request.POST['numero2'],
        'oprc': request.POST['oprc'],
        'total': total,
    }
    
    return render(request, 'operaciones/resultado.html',context)
