from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (TemplateView,ListView,CreateView,DeleteView,UpdateView,DetailView)
from . import models


class ContaListView(ListView):
    template_name = 'crud_app/tabela.html'
    model = models.Conta

#    def get_queryset(self):
#        user = self.request.user
#        return user.fornecedor.all()
#
class ContaCreateView(CreateView):
    template_name = 'crud_app/tabela.html'
    fields = ("desc","fornecedor")
    model = models.Conta
    success_url = reverse_lazy("crud_app:list")

class ContaDeleteView(DeleteView):
     model = models.Conta
     template_name= 'crud_app/excluir-cadastro.html'
     success_url = reverse_lazy("crud_app:list")

class ContaUpdateView(UpdateView):
    template_name = 'crud_app/cadastro.html'
    fields = ("desc","fornecedor")
    model = models.Conta
    success_url = reverse_lazy("crud_app:list")

class ContaDetailView(DetailView):
    model = models.Conta 
    template_name = 'crud_app/detail.html'


def create_list(request):
    name = request.POST.get('')