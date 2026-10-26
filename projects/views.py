from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from projects.models import Project


# Create your views here.
class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'


class ProjectCreateView(CreateView):
    model = Project
    fields = ["name", "description" , "start_date", "end_date", "status"]
    success_url = reverse_lazy("projects:list")

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ["name", "description" , "start_date", "end_date", "status"]
    success_url = reverse_lazy("projects:list")

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("projects:list")


