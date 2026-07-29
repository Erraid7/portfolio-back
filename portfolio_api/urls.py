from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home_view),
    path("about/", views.about_view),
    path("projects/", views.projects_list_view),
    path("projects/<int:pk>/", views.project_detail_view),
    path("skills/", views.skills_view),
    path("experience/", views.experience_view),
    path("services/", views.services_view),
    path("contact/", views.contact_view),
    path("auth/login/", views.login_view),
]