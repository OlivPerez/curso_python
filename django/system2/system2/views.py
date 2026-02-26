
from django.http import HttpResponse    # para devolver respuestas HTTP simples
from django.template import loader      # cargador de plantillas de Django
from django.shortcuts import render     # combina plantillas con contexto y devuelve una respuesta
import datetime                         # módulo datetime para trabajar con fechas y horas


number_list = [45, 30, 200] # Lista de números

# Vista que recibe un número y verifica si está en la lista
def check(request, n):
    if(n in number_list): # si el número está en la lista
        message = "el numero si existe en la lista"
    else: # Si no está en la lista
        message = "el numero no existe en la lista"
    return HttpResponse(message)    # al final evuelve la respuesta HTTP con el mensaje

# Vista que muestra la fecha y hora actual
def date_time(request):
    
    now = datetime.datetime.now()           # Obtiene la fecha y hora actual
    html = "<h1> Hoy es el %s. </h1>" % now # Crea un HTML simple con la fecha y hora
    return HttpResponse(html)               # Devuelve la respuesta HTTP con el HTML generado

# Vista que carga y renderiza la plantilla index.html
def template_index(request):
    
    template = loader.get_template("index.html")    # Carga la plantilla usando loader
    document = template.render()                    # Renderiza la plantilla sin contexto adicional
    return HttpResponse(document)                   # Devuelve la respuesta HTTP con el documento renderizado

# Vista que renderiza directamente la plantilla login.html
def template_login(request):
    # Usa la función render para devolver la plantilla login.html
    return render(request, "login.html")
