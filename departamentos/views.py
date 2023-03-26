from django.urls import reverse_lazy
from .models import Departamento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.


class DepartamentoList(ListView):
    model = Departamento
    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)
    

class DepartamentoCreat(CreateView):
    model = Departamento
    fields = ['name']
    
    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreat, self).form_valid(form)
    
    
class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ['name']
    
    
class DepartamentoDelet(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamento')