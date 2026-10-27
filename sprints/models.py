from django.db import models

from projects.models import Project


# Create your models here.
class Sprint(models.Model):
    class StatusChoices(models.TextChoices):
        PLANNED = 'planned', 'Planned'
        ACTIVE = 'active', 'Active'
        COMPLETED = 'completed', 'Completed'

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(choices=StatusChoices.choices, max_length=10)

    def __str__(self):
        return self.name

    @property
    def progress(self):

        total_tasks = self.task_set.count()

        if total_tasks == 0:
            return 0

        completed_tasks = self.task_set.filter(status='completed').count()
        return round((completed_tasks / total_tasks) * 100)
