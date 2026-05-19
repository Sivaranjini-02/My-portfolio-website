from django.db import models

class About(models.Model):
    name=models.CharField(max_length=200)
    description = models.TextField()
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)  # Optional: PDF resume
    # Professional Links
    linkedin_url = models.URLField(blank=True)

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='projects/')

class Skill(models.Model):
    title=models.CharField(max_length=200)

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=15)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)