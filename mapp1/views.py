from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first(request):
    return HttpResponse('muni ganendra')
def second(request):
    return HttpResponse('<h1><marquee>is a bad boy</marquee></h1>')    