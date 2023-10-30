from django.db import models
# authentication/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class PetBoardingBooking(models.Model):
    pet_name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=20)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    special_requests = models.TextField(blank=True)
    owner_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.pet_name

# Model for Pet Vet Appointment
class PetVetAppointment(models.Model):
    pet_name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=20)
    appointment_date = models.DateField()
    reason_for_visit = models.TextField()
    owner_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.pet_name

# Model for Pet Grooming Appointment
class PetGroomingAppointment(models.Model):
    pet_name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=20)
    appointment_date = models.DateField()
    special_requests = models.TextField()
    owner_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.pet_name

