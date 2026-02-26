from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def pancito(request): # importante, siempre poner request dentro de los parentesis
    message = "pancito"
    return HttpResponse(message) # el retorno se hace con HttpResponse

def fibonacci(request):
    series = []
    a = 0
    b = 1

    while(a <= 100):
        series.append(a)
        series.append(", ")
        c = a + b
        a = b
        b = c
    series.pop()
    return HttpResponse(series)

@login_required
def lorem_ipsum(request):
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    return HttpResponse(text)