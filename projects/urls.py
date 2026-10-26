from django.urls import path, include

from projects.views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectDeleteView, ProjectUpdateView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='list'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('',  ProjectDetailView.as_view(), name='detail'),
        path('edit/', ProjectUpdateView.as_view(), name='update'),
        path('delete/', ProjectDeleteView.as_view(), name='delete'),
    ])),
]