from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.http import HttpResponseRedirect
import requests


#url='https://covid19.th-stat.com/api/open/today'



# Create your views here.
def index(request):
    today=(requests.get('https://covid19.th-stat.com/api/open/today')).json()
    Sum=(requests.get('https://covid19.th-stat.com/api/open/cases/sum')).json()
    return render(request, 'index.html', {"all" : today,"all2" : Sum})

    
def about(request):
    return render(request, 'about.html')

    
def contact(request):
    today=(requests.get('https://covid19.th-stat.com/api/open/today')).json()
    Sum=(requests.get('https://covid19.th-stat.com/api/open/cases/sum')).json()
    
    return render(request, 'contact.html', {"all" : today,"all2" : Sum})
def news(request):
    News=(requests.get('http://newsapi.org/v2/top-headlines?country=th&apiKey=a70d4f9ca8894cf09976575575426bcb')).json()
    
    return render(request, 'news.html',{"all": News})    
def delete(request, itemID):
    item = List.objects.get(pk=itemID)
    item.delete()
    return redirect('index')
def Uncross(request, itemID):
    item= List.objects.get(pk=itemID)
    item.finished = not item.finished
    item.save()
    return redirect('index')   