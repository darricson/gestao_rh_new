from django.urls import path, include
from .views import FuncionariosList

urlpatterns = [
    path('funcionarios', FuncionariosList.as_view(), name='list_funcionarios'),
]
