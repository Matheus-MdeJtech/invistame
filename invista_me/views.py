from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/investimentos.html', dados)

def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento) # Busque na tabela investimento aquele que tenha a chave primaria igual aid_investimento    
    }
    return render(request, 'investimentos/detalhe.html', dados)

@login_required
def criar(request):
    if request.method == 'POST': # Se estiver enviando dados atraves do POST
        investimento_form = InvestimentoForm(request.POST) # Vai Obter os dados
        if investimento_form.is_valid(): # Verifica se sao validos
            investimento_form.save()# Salva no banco
        return redirect(investimentos) # Redireciona para outra tela

    else: # seFor a primeira vez
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form}
        return render(request,'investimentos/novo_investimento.html', context=formulario)

@login_required
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)

    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento) # Cria um novo formulario ja com os valores preenchidos, valores de investimento
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    
    elif request.method == 'POST':
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')
    
@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        Investimento.delete(investimento)
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})

