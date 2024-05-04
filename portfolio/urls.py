from django.urls import path
from . import views
from .views import get_projects

urlpatterns = [
    path("", views.home, name="home"),
    path("todos", views.todos, name="Todos"),
    path("index", views.index, name="Portfolio"),
    path("projects/", get_projects, name="get_projects"),
    path('project/<str:project_name>/', views.projDetails, name='project_details'),
    path("about_me", views.about_me, name="about_me"),

]


