from django.urls import path

from sprints.views import SprintListView

app_name = 'sprints'
urlpatterns = [
    path('', SprintListView.as_view(), name='list'),
]