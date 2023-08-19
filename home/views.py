from django.shortcuts import render, HttpResponse


def index(request):
    context = {
        'variable': "this is a variable text",
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is About")

def about(request):
    return HttpResponse("This is About")

def services(request):
    return HttpResponse("This is Services")

def contact(request):
    return HttpResponse("This is Contact")
