from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import PetBoardingBookingForm  # Import the correct form
from .models import PetBoardingBooking
from .forms import PetVetAppointmentForm, PetGroomingAppointmentForm
from .models import PetVetAppointment, PetGroomingAppointment



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')

from django.shortcuts import render, redirect

# ... Other view functions ...

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # Correctly use 'password' instead of 'pass'

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'index.html')


def HomePage(request):
    username = request.session.get('username')  # Retrieve the username from the session
    print("Session Username:", username)  # Check if the session value is being retrieved
    context = {'username': username}
    return render(request, 'index.html', context)
def logout_user(request):
    logout(request)
    return redirect('index') 


  # Import the correct model
@login_required
def boarding_service(request):
    if request.method == 'POST':
        form = PetBoardingBookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the "finalproject2" database
            return redirect('index')  # Redirect to a success page
    else:
        form = PetBoardingBookingForm()
    
    context = {'form': form}
    return render(request, 'boarding.html', context)  


def submit_booking_view(request):
    if request.method == 'POST':
    
     return HttpResponse("Form submitted successfully!")  

    return HttpResponse("Invalid request method!")


# View for Pet Vet Appointment
@login_required
def vet_appointment(request):
    if request.method == 'POST':
        form = PetVetAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page
    else:
        form = PetVetAppointmentForm()
    
    context = {'form': form}
    return render(request, 'vet.html', context)

# View for Pet Grooming Appointment

def grooming_appointment(request):
    if request.method == 'POST':
        form = PetGroomingAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page
    else:
        form = PetGroomingAppointmentForm()
    
    context = {'form': form}
    return render(request, 'grooming.html', context)


