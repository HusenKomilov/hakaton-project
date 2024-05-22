from django.urls import path
from hospital import views

urlpatterns = [
    path("", views.HospitalListAPIView.as_view()),
    path("<int:pk>/", views.HospitalRetriveAPIView.as_view()),
]
