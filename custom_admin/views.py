from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AdminLoginForm, ProjectForm, SkillForm, ServiceForm, ExperienceForm, ResumeForm
from core.models import Project, Skill, Service, ContactMessage, Experience, Resume

def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('custom_admin:dashboard')
    
    if request.method == 'POST':
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                login(request, user)
                return redirect('custom_admin:dashboard')
            else:
                messages.error(request, 'Access denied. Admin privileges required.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AdminLoginForm()
    
    return render(request, 'custom_admin/login.html', {'form': form})

@login_required
def admin_logout(request):
    logout(request)
    return redirect('custom_admin:login')

@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return redirect('custom_admin:login')
        
    context = {
        'projects_count': Project.objects.count(),
        'skills_count': Skill.objects.count(),
        'services_count': Service.objects.count(),
        'messages_count': ContactMessage.objects.count(),
        'recent_messages': ContactMessage.objects.order_by('-sent_at')[:5]
    }
    return render(request, 'custom_admin/dashboard.html', context)

# --- Project Views ---
@login_required
def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'custom_admin/project_list.html', {'projects': projects})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project created successfully.')
            return redirect('custom_admin:project_list')
    else:
        form = ProjectForm()
    return render(request, 'custom_admin/project_form.html', {'form': form, 'title': 'Create Project'})

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully.')
            return redirect('custom_admin:project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'custom_admin/project_form.html', {'form': form, 'title': 'Update Project'})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully.')
        return redirect('custom_admin:project_list')
    return render(request, 'custom_admin/project_confirm_delete.html', {'project': project})

# --- Skill Views ---
@login_required
def skill_list(request):
    skills = Skill.objects.all().order_by('-proficiency')
    return render(request, 'custom_admin/skill_list.html', {'skills': skills})

@login_required
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill created successfully.')
            return redirect('custom_admin:skill_list')
    else:
        form = SkillForm()
    return render(request, 'custom_admin/skill_form.html', {'form': form, 'title': 'Create Skill'})

@login_required
def skill_update(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully.')
            return redirect('custom_admin:skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'custom_admin/skill_form.html', {'form': form, 'title': 'Update Skill'})

@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully.')
        return redirect('custom_admin:skill_list')
    return render(request, 'custom_admin/skill_confirm_delete.html', {'skill': skill})

# --- Service Views ---
@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'custom_admin/service_list.html', {'services': services})

@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service created successfully.')
            return redirect('custom_admin:service_list')
    else:
        form = ServiceForm()
    return render(request, 'custom_admin/service_form.html', {'form': form, 'title': 'Create Service'})

@login_required
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully.')
            return redirect('custom_admin:service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'custom_admin/service_form.html', {'form': form, 'title': 'Update Service'})

@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service deleted successfully.')
        return redirect('custom_admin:service_list')
    return render(request, 'custom_admin/service_confirm_delete.html', {'service': service})

# --- Contact Message Views ---
@login_required
def contact_list(request):
    messages_list = ContactMessage.objects.all().order_by('-sent_at')
    return render(request, 'custom_admin/contact_list.html', {'messages_list': messages_list})

@login_required
def contact_detail(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    return render(request, 'custom_admin/contact_detail.html', {'message': message})

@login_required
def contact_delete(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Message deleted successfully.')
        return redirect('custom_admin:contact_list')
    return render(request, 'custom_admin/contact_confirm_delete.html', {'message': message})

# --- Experience Views ---
@login_required
def experience_list(request):
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'custom_admin/experience_list.html', {'experiences': experiences})

@login_required
def experience_create(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experience created successfully.')
            return redirect('custom_admin:experience_list')
    else:
        form = ExperienceForm()
    return render(request, 'custom_admin/experience_form.html', {'form': form, 'title': 'Add Experience'})

@login_required
def experience_update(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experience updated successfully.')
            return redirect('custom_admin:experience_list')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'custom_admin/experience_form.html', {'form': form, 'title': 'Update Experience'})

@login_required
def experience_delete(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        experience.delete()
        messages.success(request, 'Experience deleted successfully.')
        return redirect('custom_admin:experience_list')
    return render(request, 'custom_admin/experience_confirm_delete.html', {'experience': experience})

# --- Resume Views ---
@login_required
def resume_list(request):
    resumes = Resume.objects.all().order_by('-updated_at')
    return render(request, 'custom_admin/resume_list.html', {'resumes': resumes})

@login_required
def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume uploaded successfully.')
            return redirect('custom_admin:resume_list')
    else:
        form = ResumeForm()
    return render(request, 'custom_admin/resume_form.html', {'form': form, 'title': 'Upload Resume'})

@login_required
def resume_delete(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == 'POST':
        resume.delete()
        messages.success(request, 'Resume deleted successfully.')
        return redirect('custom_admin:resume_list')
    return render(request, 'custom_admin/resume_confirm_delete.html', {'resume': resume})
