from rest_framework import generics
from hospital import models, serializers


class HospitalListAPIView(generics.ListAPIView):
    queryset = models.Hospital.objects.all().order_by("-visitors")
    serializer_class = serializers.HospitalSerializer


class HospitalRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.HospitalSerializer

    def get_object(self):
        visitor = models.Hospital.objects.get(pk=self.kwargs['pk'])
        visitor.visitors += 1
        visitor.save()
        return visitor