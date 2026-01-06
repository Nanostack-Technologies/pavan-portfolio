from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('experience/', views.experience, name="experience"),
    path('projects/', views.project_list, name="projects"),
    path('projects/<slug:slug>/', views.project_detail, name="project_detail"),
    path('contact/', views.contact, name="contact"),
]
