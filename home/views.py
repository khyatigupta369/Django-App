from django.shortcuts import render, HttpResponse


def index(request):
    context = {
        'variable': "this is a variable text",
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Home")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is Services")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is Contact")
