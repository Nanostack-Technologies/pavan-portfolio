from django.urls import path
from . import views

app_name = 'custom_admin'

urlpatterns = [
    path('', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Project URLs
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/update/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    
    # Skill URLs
    path('skills/', views.skill_list, name='skill_list'),
    path('skills/create/', views.skill_create, name='skill_create'),
    path('skills/<int:pk>/update/', views.skill_update, name='skill_update'),
    path('skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
    
    # Service URLs
    path('services/', views.service_list, name='service_list'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:pk>/update/', views.service_update, name='service_update'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),

    # Contact Message URLs
    path('messages/', views.contact_list, name='contact_list'),
    path('messages/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('messages/<int:pk>/delete/', views.contact_delete, name='contact_delete'),

    # Experience URLs
    path('experience/', views.experience_list, name='experience_list'),
    path('experience/create/', views.experience_create, name='experience_create'),
    path('experience/<int:pk>/update/', views.experience_update, name='experience_update'),
    path('experience/<int:pk>/delete/', views.experience_delete, name='experience_delete'),

    # Resume URLs
    path('resumes/', views.resume_list, name='resume_list'),
    path('resumes/create/', views.resume_create, name='resume_create'),
    path('resumes/<int:pk>/delete/', views.resume_delete, name='resume_delete'),
]
