from django.shortcuts import render

def home(request):
    return render(request, "simplepages/home.html")

def contact_us(request):
    return render(request, "simplepages/contact_us.html")

def about_us(request):
    return render(request, "simplepages/about_us.html")