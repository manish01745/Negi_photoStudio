from django.contrib import admin
from . models import ContactForm,Project,ProjectImage

# Register your models here.
admin.site.register(ContactForm)
admin.site.register(Project)
admin.site.register(ProjectImage)
