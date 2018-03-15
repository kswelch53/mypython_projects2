from django.shortcuts import render, HttpResponse, redirect


def index(request):
    print("This is index method in Landing Page views.py")
    return render(request, 'app1_landingpage/index.html')

    
