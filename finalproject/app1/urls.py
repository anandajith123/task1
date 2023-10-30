from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.HomePage, name="index"),         # Assuming you have an 'index' view in views.py
    path('login/', views.LoginPage, name="login"),     # Assuming 'login_view' is your login view
    path('signup/', views.SignupPage, name="signup"),  # Assuming 'signup_view' is your signup view
    path('logout/', views.logout_user, name='logout'),
    path('boarding/', views.boarding_service, name='boarding'),
    path('vet/', views.vet_appointment, name='vet'),
    path('grooming/', views.grooming_appointment, name='grooming'),
    path('submit_booking/', views.submit_booking_view, name='submit_booking')
]
