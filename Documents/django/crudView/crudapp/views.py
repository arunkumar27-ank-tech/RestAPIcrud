from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Todo


class viewlist(ListView):
    model = Todo
    template_name = 'crudapp/list.html'

class detailview(DetailView):
    model = Todo
    template_name = 'crudapp/detail.html'
    context_object_name = 'object'

class createview(CreateView):
    model = Todo
    template_name = 'crudapp/create.html'
    fields = '__all__'
    success_url = reverse_lazy('view')


class updateview(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('view')
    template_name = 'crudapp/update.html'

class deleteview(DeleteView):
    model = Todo
    template_name = 'crudapp/delete.html'
    success_url = reverse_lazy('view')
    context_object_name = 'object'

# Create your views here.
