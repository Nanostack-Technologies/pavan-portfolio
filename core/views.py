from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Project, Skill, Service, ContactMessage, Experience, Resume

def home(request):
    projects = Project.objects.all().order_by('-created_at')[:3]
    resume = Resume.objects.last()
    context = {
        "projects": projects,
        "resume": resume,
    }
    return render(request, "pages/home.html", context)

def about(request):
    skills = Skill.objects.all().order_by('-proficiency')
    services = Service.objects.all()
    return render(request, "pages/about.html", {
        "skills": skills,
        "services": services
    })

def experience(request):
    experiences = Experience.objects.all()
    resume = Resume.objects.last()
    return render(request, "pages/experience.html", {
        "experiences": experiences,
        "resume": resume
    })

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, "pages/projects.html", {"projects": projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "pages/project_detail.html", {"project": project})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!")
    
    return render(request, "pages/contact.html")

def custom_404(request, exception):
    return render(request, "pages/404.html", status=404)