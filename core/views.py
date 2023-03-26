from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from funcionarios.models import Funcionario

# Create your views here.

# @ força a acessar a aplicação somente quando user estiver autenticado
@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)