from django.http import request, response
from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

#def index(request):
#   return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")    
    return redirect('/')    

#força esta com login ativo, caso não esteja logado leva para a tela de login
@login_required(login_url='/login/')
def lista_eventos(request):
    # capturando os dados
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    #evento = Evento.objects.all()
    dados = {'eventos' :evento}
    return render(request, 'agenda.html', dados)
 


