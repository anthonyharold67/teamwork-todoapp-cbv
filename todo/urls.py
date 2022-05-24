from django.urls import path, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView
from .forms import TodoForm

from .models import Todo
from .views import Home, TodoCreate, TodoDelete, TodoDetail, TodoList, TodoUpdate

urlpatterns = [
    path("",Home.as_view(),name="home"),
    # path("",TemplateView.as_view(template_name = 'todo/home.html'),name="home"),

    path("list/",TodoList.as_view(),name="list"),
    # path("list/",ListView.as_view(template_name = 'todo/todo_list.html',model = Todo),name="list"),

    path("add/",TodoCreate.as_view(),name="add"),
    # path("add/",CreateView.as_view(template_name = 'todo/todo_add.html',model = Todo,form_class = TodoForm,success_url=reverse_lazy("list")),name="add"),

    path("update/<int:pk>/",TodoUpdate.as_view(),name="update"),
    # path("update/<int:id>/",TodoUpdate.as_view(),name="update"),#urls.py içinde id parametresi ile işlem yapmak istiyorsak bunu views.py de declare ediyoruz şu şekilde pk_url_kwarg="id"
    # path("update/<int:pk>/",UpdateView.as_view(model = Todo,form_class = TodoForm,template_name = 'todo/todo_update.html',success_url=reverse_lazy("list")),name="update"),

    path("delete/<int:pk>/",TodoDelete.as_view(),name="delete"),
    # path("delete/<int:pk>/",DeleteView.as_view(model = Todo,template_name = 'todo/todo_delete.html',success_url=reverse_lazy("list")),name="delete"),

    path("detail/<int:pk>/",TodoDetail.as_view(),name="detail"),
    # path("detail/<int:pk>/",DetailView.as_view(model = Todo,template_name = 'todo/todo_detail.html'),name="detail"),
]
