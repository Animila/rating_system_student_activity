from django.shortcuts import render
from cabinet.models import Event, DataUser

def home(request):
    data = Event.objects.all()
    user = DataUser.objects.all()
    group = user.get(pk=1)



    return render(request, 'home/index.html', {'data': data, 'group': group.group})