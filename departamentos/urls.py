from django.urls import path
from .views import (DepartamentoList, DepartamentoCreat, 
                    DepartamentoEdit, DepartamentoDelet)


urlpatterns = [
    path('list', DepartamentoList.as_view(), name='list_departamento'),
    path('novo', DepartamentoCreat.as_view(), name='creat_departamento'),
    path('editar<int:pk>', DepartamentoEdit.as_view(), name='edit_departamento'),
    path('deletar<int:pk>', DepartamentoDelet.as_view(), 
         name='delet_departamento'),

]