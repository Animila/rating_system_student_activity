from django.shortcuts import render
from .models import News

def home(request):
    data = News.objects.all()
    return render(request, 'home/index.html', {'data': data})