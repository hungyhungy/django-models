from django.shortcuts import render
from .models import Room
# rooms = [
#     {'id':1, 'name':'Python programing'},
#     {'id':2, 'name':'Java programing'},
#     {'id':3, 'name':'C++ programing'},
# ]


# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'room.html', context)