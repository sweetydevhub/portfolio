from django.shortcuts import render, HttpResponse
from home.models import Contact


# Create your views here.
def home(request):
    context = {'name': 'Sweety', 'course': 'Python'}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("this is my Conatact Details. (/contact)")
    return render(request, 'contact.html')     

def projects(request):
    # return HttpResponse("this is my Project data. (/projects)")
    if request.method == "POST":
    
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        desc = request.POST['desc']
        print(name,phone, email, desc)
    return render(request, 'projects.html')