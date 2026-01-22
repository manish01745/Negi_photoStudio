from django.urls import path
from . import views
from .views import Portfolio_detail

urlpatterns = [
    path('', views.Home, name='Home'),
    path('about', views.About, name='About'),
    path('services', views.Services, name='Services'),
    path('contact', views.ContactDetail, name='Contact'),
    path('portfolio', views.Portfolio, name='Portfolio'),
     path('<str:category>/',views.Portfolio, name='portfolio_with_category'), 
     path('portfolio/<slug:slug>/', Portfolio_detail, name='portfolio_detail'),
    path('pricing', views.Pricing, name='Pricing'),
    path('testimonial', views.Testimonial, name='Testimonial')
]
