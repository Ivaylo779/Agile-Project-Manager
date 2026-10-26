from django.urls import path

from tasks.views import TaskListView, LabelListView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('labels/', LabelListView.as_view(), name='label_list'),
]