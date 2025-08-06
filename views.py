from django.shortcuts import render
from contactinfo.models import Contactdetails
from saveform.models import SaveDetails
from registrations.models import RegistrationDetails



def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def formpage(request):
    return render(request, 'form.html')


def contactEnquiry(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        # print(name)
        # print(email)
        # print(phone)
        en = SaveDetails(fname=name, Email=email, phone=phone )
        en.save()

        context = { "message" : "Thank you for your enquiry!"  }       
        return render(request, 'form.html', context)
    return render(request, 'form.html')

def contactus(request):
    return render(request, 'contact.html')

def saveinfo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name)
        print(email)
        print(subject)
        print(message)
        en = Contactdetails(fname=name, Email=email, Subject=subject,
                         Message=message)
        en.save()
        context = { "message" : "Form Submitted succesfully !"  } 
        return render(request, 'contact.html', context )
    return render(request, 'contact.html')


def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        language = request.POST.getlist('language') 

        print(name)
        print(phone)    
        print(email)
        print(password)
        print(dob)
        print(gender)
        print(language)

        en = RegistrationDetails(name=name, email=email,phone=phone, password=password, 
                                 dob=dob, gender=gender, language=','.join(language))
        en.save()

        context = { "message" : "Form Submitted successfully!" } 
        return render(request, 'registration.html', context)
    
    return render(request, 'registration.html')



