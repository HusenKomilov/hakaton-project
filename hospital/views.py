from rest_framework import generics
from hospital import models, serializers


class HospitalListAPIView(generics.ListAPIView):
    queryset = models.Hospital.objects.all()
    # annotate(
    #     gallery=models.HospitalGallery.objects.all())
    serializer_class = serializers.HospitalSerializer
