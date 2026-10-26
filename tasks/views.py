from django.shortcuts import render
from django.views.generic import ListView

from tasks.models import Task, Label


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    context_object_name = 'tasks'

class LabelListView(ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'