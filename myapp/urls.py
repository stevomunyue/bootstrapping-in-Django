# myapp/urls.py  
from django.urls import path  
from . import views  

urlpatterns = [  
    path('', views.index, name='index'),  # Root URL for index  
    path('index.html', views.index, name='index_html'),  # Optional: handle index.html  
    path('about.html', views.about, name='about'),  
    path('agents.html', views.agents, name='agents'),  
    path('contact.html', views.contact, name='contact'),  
    path('properties.html', views.properties, name='properties'),  
    path('property-single.html', views.property_single, name='property_single'),  
    path('services.html', views.services, name='services'),  
    path('service-details.html', views.service_details, name='service_details'),  
    path('starter-page', views.starter_page, name='starter_page'),  
]