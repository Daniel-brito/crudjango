from django.http import response
from django.shortcuts import redirect, render
from core.models import Evento

# Create your views here.

#def index(request):
#   return redirect('/agenda/')

def lista_eventos(request):
    # capturando os dados
    # usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()
    dados = {'eventos' :evento}
    return render(request, 'agenda.html', dados)
 


