from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    print('request',request.GET.get('length',12))
    characters=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length',12))
    thepassword=''
    if request.GET.get('uppercase'):
            characters.extend(list('ABCDEFGHIGKLMNOPQRSTVUWXYZ'))

    if request.GET.get('specials'):
            characters.extend(list('£$%^&*(@!)'))
            
    if request.GET.get('numbers'):
            characters.extend(list('0123456789'))

    for x in range(length):
        thepassword+=random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})

def aboutus(request):
    return render(request,'generator/aboutus.html')
    