from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader


def home(request):
    return render(request, 'default/home.html')
