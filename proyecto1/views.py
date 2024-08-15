from django.http import HttpResponse
from datetime import datetime, date
from django.template import Template, Context
from django.shortcuts import render
from django.template import loader
from AppCoder.models import Curso

def saludo(request):

    return HttpResponse("Hola Django - Coder")

def otra_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.</p>")

def dia_de_hoy(request):
    hoy = date.today()
    return HttpResponse(f"Hoy es {hoy}")

def muestra_nombre(self, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")

def probando_template(request):

    nom = "Kily"
    ap = "Sanchez"

    lista_de_notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    diccionario = {'nombre': nom, 'apellido': ap, 'hoy': datetime.now(), "notas": lista_de_notas}
    
    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def agregar_curso(request, nom, cam): #se agrega el curso a la base de datos y muestra el mensaje(no es buena practica que alguien agregue informacion por url pero es para practicar)
    curso = Curso(nombre=nom, camada=cam)
    curso.save()

    return HttpResponse("Curso agregado")




