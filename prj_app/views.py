from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib import messages
import requests
import geopy
import folium
import os
from .models import register
from django.shortcuts import render, redirect
from .utils import send_otp, verify_otp
#from .forms import RegistrationForm
#from .models import YourModel
from .forms import RegistrationForm
import firebase_admin


# Create your views here.
def map_view(request):
    return render(request,'current_location_map.html')
def index(request):
    directory = "C:/Users/jerin/Downloads/BusTrackingSystem/prj_app/Templates/"
    geolocator = geopy.Nominatim(user_agent="Nikki")
    current_location='Kottayam'
    response = requests.get(f"https://nominatim.openstreetmap.org/search?q={current_location}&format=json&limit=1", verify=False)
    location_data = response.json()[0]
    latitude = float(location_data['lat'])
    longitude = float(location_data['lon'])
    map = folium.Map(location=[latitude, longitude], zoom_start=13)
    folium.Marker([latitude, longitude], popup='Your Current Location').add_to(map)
    map.save(directory +"current_location_map.html")
    with open("current_location_map.html", "r") as file:
        html_content = file.read()

    print(html_content)
    return render(request,'Index.html',{}) 
def find_bus(request):
    return render(request,'find_bus.html')

def user_register(request):
    return render(request,'User_registration.html')



def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save user data to the database
            #form.save()
            print('hai')
            form.save()
            request.session['registration_complete'] = True
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            # Now you can save these values to your model
            #return HttpResponse()
            #return render(request,'index.html')  # Redirect to success page
            messages.success(request, "Registration successfull!..")
    else:
        form = RegistrationForm()
    return render(request, 'User_registration.html', {'form': form})

def modal_login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        
        if email and password:
            # Check if the user is a superuser
            if User.objects.filter(email=email, is_superuser=True).exists():
                # Authenticate as a superuser
                user = authenticate(request, username=email, password=password)
                return redirect("adminpage")
            else:
                # Authenticate regular user
                user = authenticate(request, username=email, password=password)

        if email and password:
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                request.session['email'] = user.email
                return redirect('../')  # Redirect to index page after successful login
            else:
                error = "Invalid email or password. Please try again."
                messages.error(request, error)
        if phone:
            phone = request.POST.get('phone')
            verification_id = send_otp(phone)
            request.session['verification_id'] = verification_id
            return render(request, 'verify_otp.html')
        return render(request, 'Index.html')
            


    else:
        # If the request method is not POST, or if email and password are not provided,
        # render the login page again
        return render(request, 'login.html')

    # If authentication fails or no data provided, render the login page again
    return render(request, 'login.html')
        
            


def system_admin(request):
    return render(request,'Admin.html')

def bus_provider(request):
    return render(request,'Bus_provider.html')

def logout_view(request):
    # Clear all session data
    request.session.flush()

    # Redirect to a success page, or wherever you want
    return redirect('../')


def send_otp_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        verification_id = send_otp(phone_number)
        request.session['verification_id'] = verification_id
        return render(request, 'verify_otp.html')
    return render(request, 'send_otp.html')

def verify_otp_view(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        verification_id = request.session.get('verification_id')
        if verification_id:
            is_valid = verify_otp(verification_id, otp)
            if is_valid:
                # OTP verification successful, perform login
                return render(request, 'login_success.html')
            else:
                # OTP verification failed
                return render(request, 'login_failure.html')
        else:
            # Session expired or verification ID not found
            return render(request, 'session_expired.html')
    return render(request, 'verify_otp.html')

class Adminview(TemplateView):
    template_name="Admin.html"