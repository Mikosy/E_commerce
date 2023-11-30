from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')

def registerView(request):
    return render(request, 'app/register.html')