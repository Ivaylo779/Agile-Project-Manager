from django.views.generic import TemplateView

from tasks.models import Task


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    context_object_name = 'dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_tasks"] = (
            Task.objects.select_related("sprint").order_by("-created_at")[:5])
        return context