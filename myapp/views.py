# myapp/views.py  
from django.shortcuts import render 
 

def index_html(request):  
    return render(request, 'myapp/index.html')  # Update the path to your actual template 

def base(request):  
    return render(request, 'myapp/base.html')  
def index(request):  
    return render(request, 'myapp/index.html')  

def about(request):  
    return render(request, 'myapp/about.html')  

def agents(request):  
    return render(request, 'myapp/agents.html')  

def contact(request):  
    return render(request, 'myapp/contact.html')  

def properties(request):  
    return render(request, 'myapp/properties.html')  

def property_single(request):  
    return render(request, 'myapp/property-single.html')  

def service_details(request):  
    return render(request, 'myapp/service-details.html')  

def services(request):  
    return render(request, 'myapp/services.html')  

def starter_page(request):  
    return render(request, 'myapp/starter-page.html')