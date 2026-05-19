from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Project,Skill,About,Contact,ContactMessage
def home(request):
    return render(request,'home.html')

def about(request):
    about_data=About.objects.first()
    return render(request,'about.html',{'about':about_data})

def projects(request):
    project=Project.objects.all()
    return render(request,'project.html',{'projects':project})

def skills(request):
    skill=Skill.objects.all()
    return render(request,'skills.html',{'skills':skill})

# Replace both contact functions with just this ONE:
def contact(request):

    contact_data = Contact.objects.first()


    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')


        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('/contact/')


    return render(request, 'contact.html', {'contact': contact_data})