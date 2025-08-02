from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myhome(request):
    return HttpResponse("hello EB! its fun learning cloud")