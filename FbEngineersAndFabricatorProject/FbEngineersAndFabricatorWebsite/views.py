from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ContactUs(request):
    return render(request, 'contactus.html')

def Products(request):
    return render(request, 'products.html')

def AboutUs(request):
    return render(request, 'aboutus.html')