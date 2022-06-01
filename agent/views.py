from django.shortcuts import render

from agent.models import Contato, Servicos

# Create your views here.

def index(request):
    data = Servicos.objects.first()
    con = Contato.objects.first()
    return render(request,'index.html',{'data':data,'con':con})

def contato(request):
    return render(request, 'index_contato.html')


def agente(request):
    return render(request, 'index_agente.html')


def servico(request):
    return render(request, 'index_servicos.html')