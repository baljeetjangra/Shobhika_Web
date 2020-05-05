from django.shortcuts import render
from .models import destination


# Create your views here.
def index(request):
    dest1 = destination()
    dest1.name = 'Udaipur'
    dest1.desc = 'The City Of Lakes'
    dest1.img = 'udaipur.jpg'
    dest1.price = 500

    dest2 = destination()
    dest2.name = 'Mumbai'
    dest2.desc = 'The City never sleeps'
    dest2.img = 'mumbai.jpg'
    dest2.price = 600

    dest3 = destination()
    dest3.name = 'Jaipur'
    dest3.desc = 'The Pink City'
    dest3.img = 'hawa.jpg'
    dest3.price = 680

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})
