from django.urls import path, include

from tasks.views import TaskListView, LabelListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('', TaskDetailView.as_view(), name='detail'),
        path('edit/', TaskUpdateView.as_view(), name='update'),
        path('delete/', TaskDeleteView.as_view(), name='delete'),
    ])),
    path('labels/', LabelListView.as_view(), name='label_list'),
]