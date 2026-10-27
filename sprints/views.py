from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from sprints.models import Sprint


# Create your views here.

class SprintListView(ListView):
    model = Sprint
    context_object_name = 'sprints'
    template_name = 'sprints/sprint_list.html'

class SprintCreateView(CreateView):
    model = Sprint
    fields = '__all__'
    success_url = reverse_lazy("sprints:list")


class SprintDetailView(DetailView):
    model = Sprint
    context_object_name = 'sprint'
    template_name = 'sprints/sprint_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.task_set.all()
        return context


class SprintUpdateView(UpdateView):
    model = Sprint
    fields = '__all__'
    success_url = reverse_lazy("sprints:list")


class SprintDeleteView(DeleteView):
    model = Sprint
    success_url = reverse_lazy("projects:list")



















