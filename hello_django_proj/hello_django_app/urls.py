from django.urls import path
from .views import HomePageView, AboutPageView, ContactInfoPageView


urlpatterns = [
    path('home/', HomePageView.as_view(), name="home_view"),
    path('about/', AboutPageView.as_view(),name="resume_view"),
    path('contactInfo/', ContactInfoPageView.as_view(),name="contactInfo_view")
]