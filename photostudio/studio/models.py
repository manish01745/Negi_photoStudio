from django.db import models
from django.utils.text import slugify
import uuid

class ContactForm(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone")
    date = models.DateField(blank=True, null=True, verbose_name="Date")
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name="Location")
    budget = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=255, verbose_name="Email Address")
    referrer = models.CharField(max_length=255, blank=True, null=True, verbose_name="Referrer")
    subject = models.CharField(max_length=255, verbose_name="Subject")
    your_message = models.TextField(verbose_name="Message",blank=True,null=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[('wedding', 'Wedding'), ('haldi', 'Haldi'), ('birthday', 'Birthday')])
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            base_slug = self.slug
            unique_id = uuid.uuid4().hex[:6]
            self.slug = f"{base_slug}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='media', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.project.title