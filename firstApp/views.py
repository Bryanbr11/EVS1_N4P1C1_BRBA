
from django.shortcuts import render
from django.http import HttpResponse
import  datetime

def display(request):
    return HttpResponse("<h1>hola mundo</h1>")

def displayDatetime(request):
    dt= datetime.datetime.now()
    s = "<b>fecha y hora actual: </b>" + str(dt)
    return HttpResponse(s)


def informacion(request):
    return HttpResponse("<p> información es un conjunto organizado de datos relevantes para uno o más sujetos que extraen de él un conocimiento</p>")


# Create your views here.
