from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from utils.models import BaseModel
from hospital import choices


class Hospital(BaseModel):
    name = models.CharField(max_length=128)
    phone_number = models.CharField(unique=True, max_length=20)
    address = models.CharField(max_length=256)
    description = models.TextField()

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name


class HospitalGallery(BaseModel):
    image = models.ImageField(upload_to="hospital/")
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="gallery")
    index = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.hospital.name


class Specialty(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Doctor(BaseModel):
    name = models.CharField(max_length=256)
    phone_number = models.CharField(unique=True, max_length=20)
    descriotion = models.TextField()
    image = models.ImageField(upload_to="doctor")

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    status = models.CharField(
        max_length=128, choices=choices.StatusChoice.choices)
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="doctors")
    specialty = models.ForeignKey(
        Specialty, on_delete=models.CASCADE, related_name="specialty")

    def __str__(self):
        return self.name
