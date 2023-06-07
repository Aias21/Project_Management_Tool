from django.shortcuts import render
from django.http import HttpResponse
from pmt.models.user import User

# Create your views here.
def log_in(request):
    if 'email' in request.GET and 'password' in request.GET:
        User.objects.filter(email=request.GET['email'], password=request.GET['password'])
    else:
        return HttpResponse('Welcome!')