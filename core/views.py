from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# força a acessar a aplicação somente quando user estiver autenticado
@login_required
def home(request):
    return render(request, 'core/index.html')