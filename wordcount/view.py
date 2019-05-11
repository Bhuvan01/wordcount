from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def count(request):
    text = request.GET['text']
    count = text.split()
    return render(request,'count.html',{'text':text,'count':(len(count))})
def about(request):
    return render(request,'about.html')
