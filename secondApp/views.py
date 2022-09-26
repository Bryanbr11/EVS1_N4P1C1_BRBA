import datetime
from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse("<h1>hola mundo</h1>")

def displayDatetime(request):
    dt= datetime.datetime.now()
    s = "<b>fecha y hora actual: </b>" + str(dt)
    return HttpResponse(s)


def informacion(request):
    return HttpResponse("<p> información es un conjunto organizado de datos relevantes para uno o más sujetos que extraen de él un conocimiento</p><br></br><a>española de telecomunicaciones, con sede central en Madrid. Es la cuarta compañía de telecomunicaciones más importante de Europa y la</a><br></br><div>Países Bajos es miembro de la Unión Europea. Su capital es Ámsterdam sin</div><br></br><body>La más fácil es la de irnos a las propiedades del sistema en el que veremos información como la CPU, la RAM y la versión de Windows</body><br>/<br><strong>Un sistema (del latín systēma, y este del griego σύστημα sýstēma 'reunión</strong>")
# Create your views here.
