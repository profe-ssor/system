from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout 
from django.contrib import messages
from .forms import createuserForm

# Create your views here.
def home(request):
    
    return render(request, 'authentication/home.html' )


def register_page(request):
    form = createuserForm()
    context = {'form':form}
    if request.method=='POST':
        form = createuserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Successfully Created for'+ user)
            return redirect('login')
    return render(request, 'authentication/register.html', context )



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            messages.info(request, 'username OR password incorrect')
            return render(request, 'authentication/login.html')
    context = {}        
    return render(request, 'authentication/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

