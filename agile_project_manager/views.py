from django.views.generic import TemplateView

from projects.models import Project
from sprints.models import Sprint
from tasks.models import Task


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    context_object_name = 'dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_tasks"] = (Task.objects.select_related("sprint").order_by("-created_at")[:5])
        context["total_projects"] = Project.objects.count()
        context["active_sprints"] = Sprint.objects.filter(status=Sprint.StatusChoices.ACTIVE).count()
        context["open_tasks"] = Task.objects.exclude(status=Sprint.StatusChoices.COMPLETED).count()
        context["recent_projects"] = Project.objects.order_by("-created_at")[:5]
        return context