from rest_framework import serializers
from hospital import models


class HospitalGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HospitalGallery
        fields = ("id", "image", "index")


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialty
        fields = ("title",)


class DoctorsSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer()

    class Meta:
        model = models.Doctor
        fields = ("name", "phone_number", "descriotion",
                  "image", "start_time", "end_time", "status", "specialty")


class HospitalSerializer(serializers.ModelSerializer):
    gallery = HospitalGallerySerializer(many=True, read_only=True)
    doctors = DoctorsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Hospital
        fields = ("name", "phone_number", "address",
                  "description", "start_time", "end_time", "gallery", "doctors")
