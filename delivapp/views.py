from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return HttpResponse("Hello, world. You're at the poll index.")

def homepage(request):
  return render(request, 'homepage.html', {})

def signup(request):
  return render(request, 'signup.html', {})

def login(request):
  return render(request, 'login.html', {})

def done(request):
  return render(request, 'done.html', {})

def placeorder(request):
  return render(request, 'placeorder.html', { 'total' : 33.94})

def processing(request):
  return render(request, 'processing.html', {})
