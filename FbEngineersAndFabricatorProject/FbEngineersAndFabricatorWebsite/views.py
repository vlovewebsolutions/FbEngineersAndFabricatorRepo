from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ContactUs(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        phone = request.POST.get("Phone")
        query = request.POST.get("Query")
        # contact_detail = [name, phone, email, message]
        # contact_detail = list(contact_detail[0])
        contact_detail = 'Name: ' + name + '\n' + 'Phone: ' + str(phone) + '\n' + 'Message: ' + query
        send_mail(
            'Contact Detail of Visitor',
            contact_detail,
            'fbenggs@gmail.com',
            ['fbenggs@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Profile details Sent Successfully.')
        return render(request, 'contactus.html', {})
    else:
        return render(request, 'contactus.html', {})

def Products(request):
    return render(request, 'products.html')

def AboutUs(request):
    return render(request, 'aboutus.html')