from django.db import models

from sprints.models import Sprint
class Label(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# Create your models here.
class Task(models.Model):
    class PriorityChoices(models.TextChoices):
        LOW = 'LOW'
        MEDIUM = 'MEDIUM'
        HIGH = 'HIGH'
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(choices=PriorityChoices.choices, max_length=10)
    status = models.CharField(choices=Sprint.StatusChoices.choices, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    labels = models.ManyToManyField(Label)

