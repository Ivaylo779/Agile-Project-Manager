from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from tasks.models import Task, Label


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ["sprint", "title", "description", "priority", "status", "labels"]
    success_url = reverse_lazy('tasks:list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ["sprint", "title", "description", "priority", "status", "labels"]
    success_url = reverse_lazy('tasks:list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy("tasks:list")


class LabelListView(ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'



class LabelCreateView(CreateView):
    model = Label
    template_name = 'labels/label_form.html'
    fields = ['name', 'color']
    success_url = reverse_lazy('tasks:label_list')


class LabelUpdateView(UpdateView):
    model = Label
    template_name = 'labels/label_form.html'
    fields = ['name', 'color']
    success_url = reverse_lazy('tasks:label_list')


class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'labels/label_confirm_delete.html'
    success_url = reverse_lazy('dashboard')



