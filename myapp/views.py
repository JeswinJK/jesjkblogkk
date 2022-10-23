from django.shortcuts import render
from .forms import studentform
def home(request):
    return render(request,'home.html')
def must(request):
    return render(request,'must.html')
def food(request):
    return render(request,'food.html')
def register(request):
    myform=studentform
    return render(request,'register.html',{'form':myform})

# Create your views here.
