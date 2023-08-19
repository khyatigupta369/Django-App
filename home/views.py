from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("This is Homepage")

def about(request):
    return HttpResponse("This is About")

def services(request):
    return HttpResponse("This is Services")
