from django.urls import path, include
from .views import FuncionariosList, FuncionarioEdit, FuncionarioDelet, FuncionarioCreat
urlpatterns = [
    path('funcionarios', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name='edit_funcionarios'),
    path('delete/<int:pk>', FuncionarioDelet.as_view(), name='delet_funcionarios'),
    path('novo', FuncionarioCreat.as_view(), name='creat_funcionario'),

]

