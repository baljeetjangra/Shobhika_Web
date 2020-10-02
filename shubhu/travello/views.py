from django.shortcuts import render
from .models import Destination
from django.views.generic import ListView
from django.views.generic import DetailView

# Create your views here.
class IndexView(ListView):
    model = Destination
    template_name = 'home.html'
    ordering = ['-id']
    
class DestinationDetailView(DetailView):
    model = Destination
    template_name = "detail.html"
