from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect("/polls/")

urlpatterns = [
    path("", home_redirect), 
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
