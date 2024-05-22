from django.urls import path
from hospital import views

urlpatterns = [
    path("", views.HospitalListAPIView.as_view()),
]
