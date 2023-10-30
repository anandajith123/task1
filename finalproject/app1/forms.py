# forms.py in your app (app1/forms.py)
from django import forms
from .models import PetBoardingBooking
from .models import PetVetAppointment, PetGroomingAppointment

class PetBoardingBookingForm(forms.ModelForm):
    class Meta:
        model = PetBoardingBooking
        fields = '__all__'  # Use all fields from the model


# Form for Pet Vet Appointment
class PetVetAppointmentForm(forms.ModelForm):
    class Meta:
        model = PetVetAppointment
        fields = ['pet_name', 'pet_type', 'appointment_date', 'reason_for_visit', 'owner_name', 'email', 'phone']

# Form for Pet Grooming Appointment
class PetGroomingAppointmentForm(forms.ModelForm):
    class Meta:
        model = PetGroomingAppointment
        fields = ['pet_name', 'pet_type', 'appointment_date', 'special_requests', 'owner_name', 'email', 'phone']

