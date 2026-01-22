from django.shortcuts import render, redirect, get_object_or_404
from django.core.validators import validate_email
from django.contrib import messages
from django.conf import settings
from .models import ContactForm, Project
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.mail import send_mail




def Home(request):
    return render(request, "home.html")

def About(request):
    return render(request, "about.html")

def Services(request):
    return render(request, "services.html")

def Portfolio(request, category=None):
    if category:
        projects = Project.objects.filter(category=category).prefetch_related('media')
    else:
        projects = Project.objects.all().prefetch_related('media')
    return render(request, 'portfolio.html', {'projects': projects, 'selected_category': category})

def Portfolio_detail(request,slug):
    portfolio_item = get_object_or_404(Project, slug=slug)
    return render(request, 'portfolio_detail.html', {'portfolio_item': portfolio_item})


def Pricing(request):
    return render(request, "pricing.html")


def Testimonial(request):
    return render(request, "testimonial.html")



def send_email_to_admin(name, phone, email, date, location, budget, referrer, subject, your_message):
    admin_subject = 'New Customer Submission'
    admin_message = f'''
    New Customer Submission:
    Name: {name}
    Phone: {phone}
    Email: {email}
    Date: {date}
    Location: {location}
    Budget: {budget}
    Referrer: {referrer}
    Subject: {subject}
    Message: {your_message}
    '''
    admin_email = 'manish@isuremedia.com'
    send_mail(admin_subject, admin_message, admin_email, [admin_email])

def send_confirmation_email_to_user(name, email):
    customer_subject = 'Thank you for your submission'
    customer_message = f'''
    Dear {name},

    Thank you for contacting us. We have received your message and will get back to you soon.

    Best regards,
    Negi Dream studio
    '''
    admin_email = 'manish@isuremedia.com'
    send_mail(customer_subject, customer_message, admin_email, [email])


def ContactDetail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date = request.POST.get('date')
        location = request.POST.get('location')
        budget = request.POST.get('budget')
        referrer = request.POST.get('referrer')
        subject = request.POST.get('subject')
        your_message = request.POST.get('your_message')
        
        # Perform form validation
        if not any([name, email, phone]):
            messages.error(request, "Please fill in at least one field.")
        elif not all([name, email, phone]):
            messages.error(request, "Name, email, and phone are required.")
        elif len(name) < 3:
            messages.error(request, "Name should be at least 3 characters long.")
        elif len(phone) < 10:
            messages.error(request, "Phone number should be at least 10 characters long.")
        else:
            try:
                customer = ContactForm.objects.create(name=name, phone=phone, email=email, date=date, location=location, budget=budget, referrer=referrer, subject=subject, your_message=your_message)
                customer.save()
                send_email_to_admin(name, phone, email, date, location, budget, referrer, subject, your_message)
                send_confirmation_email_to_user(name, email)
                messages.success(request, "Your message has been sent successfully!")
                return redirect('Contact')
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
    return render(request, 'contact.html')

