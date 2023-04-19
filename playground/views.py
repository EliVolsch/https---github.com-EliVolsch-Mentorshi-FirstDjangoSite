from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
#def say_hello(request):
#    return HttpResponse('Hello World')

#this was the second example
#def say_hello(request):
#    return render(request, 'hello.html')

#def say_hello(request):
#    return render(request, 'hello.html', {'name': 'Mosh'})

def home(request):
    if request.method=='POST':
        username = request.POST['uname']
        password = request.POST['psw']
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            print('Exsists') 
            return redirect('viewmap/')
        else: 
            messages.success(request,'Die ou is nie hier nie!')
    return render(request, 'home-login.html')


def say_hello(request):
    return render(request, 'hello.html')

def turbines(request):
    return render(request, 'turbines.html')