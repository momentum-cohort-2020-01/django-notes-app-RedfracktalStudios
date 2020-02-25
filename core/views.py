from django.shortcuts import render
from django.http import HttpResponse

from core

def index(request):
  return HttpResponse('The Notes index')

# Create your views here.
