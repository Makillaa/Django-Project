from django.shortcuts import render


# from django.http import HttpResponse  # Для вывода на страницу простых вещей на html


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

