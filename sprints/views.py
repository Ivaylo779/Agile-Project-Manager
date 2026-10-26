from django.shortcuts import render
from django.views.generic import ListView

from sprints.models import Sprint


# Create your views here.

class SprintListView(ListView):
    model = Sprint
    context_object_name = 'sprints'
    template_name = 'sprints/sprint_list.html'