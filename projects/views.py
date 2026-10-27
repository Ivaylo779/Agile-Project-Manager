from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from projects.models import Project
from sprints.models import Sprint


# Create your views here.
class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Project.StatusChoices.choices
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sprints'] = Sprint.objects.filter(project=self.object)
        return context


class ProjectCreateView(CreateView):
    model = Project
    fields = ["name", "description" , "start_date", "end_date", "status"]
    success_url = reverse_lazy("dashboard")

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ["name", "description" , "start_date", "end_date", "status"]
    success_url = reverse_lazy("dashboard")

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("dashboard")
