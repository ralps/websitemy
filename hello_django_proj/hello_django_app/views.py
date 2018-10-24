from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = {"message_title" : "Favorite Quote",
                "message": "“Life is not a game of luck. If you wanna win, work hard.” – Sora"}
        return data
    
class AboutPageView (TemplateView):
    template_name = "resume.html"
    def get_context_data(self):
        data = {"message_title" : "Education",
                "message1": "Senior High School: Camarines Sur National High school",
                "message": "Elementary: Naga central School 2"}
        return data

class ContactInfoPageView (TemplateView):
    template_name = "contactInfo.html"
    def get_context_data(self):
        data = {"message_title" : "Maurice Ralph C. Fernandez",
                "message1": "Address: #4 calauag st. Naga City",
                "message2": "Email: fmauriceralph7@gmail.com",               
                "message3": "Mobile No. 09196450612"}
        return data

