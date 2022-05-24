from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView

from .forms import TodoForm
from .models import Todo
# Create your views here.

class Home(TemplateView):
    template_name = 'todo/home.html'

class TodoCreate(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_add.html'
    # Default is todo/todo_form.html.
    success_url = reverse_lazy("list")

class TodoList(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    # context_object_name = 'todos' #-context name istdeğimiz ismi veriyoruz template de karşılarken o isimle kullanılır.bunu yazmazsak default olarak todo_list ile karşılayabiliyoruz

class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_update.html'
    # Default todo/todo_update_form.html'
    #default myapp/modelname(küçükharf)_update_form.html
    success_url = reverse_lazy("list")
    # pk_url_kwarg="id" #urls te id parametresii ile işlem yapmak istiyorsak bunu declare ediyoruz.

class TodoDelete(DeleteView):
    model=Todo
    template_name = 'todo/todo_delete.html'
    # default fscohort/student_confirm_delete.html
    success_url = reverse_lazy("list")

class TodoDetail(DetailView):
    model = Todo
    # template_name = 'todo/todo_detail.html'//default ismide bu şekilde olduğu için template name i bellirtmemiize gerek yok
