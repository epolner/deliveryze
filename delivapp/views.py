from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth

def index(request):
  return HttpResponse("Hello, world. You're at the poll index.")

def homepage(request):
  return render(request, 'homepage.html', {})

def signup(request):
  return render(request, 'signup.html', {})

def login(request):
  return render(request, 'login.html', {})

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect("/")

def done(request):
  return render(request, 'done.html', {})

def placeorder(request):
  return render(request, 'placeorder.html', { 'total' : 33.94})

def processing(request):
  if request.user.is_authenticated():
    return render(request, 'processing.html', {})
  else:
    return render(request, 'signup.html', {})
