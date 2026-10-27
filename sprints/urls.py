from django.urls import path, include

from sprints.views import SprintListView, SprintCreateView, SprintDetailView, SprintUpdateView, SprintDeleteView

app_name = 'sprints'
urlpatterns = [
    path('', SprintListView.as_view(), name='list'),
    path('create/', SprintCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('', SprintDetailView.as_view(), name='detail'),
        path('edit/', SprintUpdateView.as_view(), name='update'),
        path('delete/', SprintDeleteView.as_view(), name='delete'),
    ]),)
]