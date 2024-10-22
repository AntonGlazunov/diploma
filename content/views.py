from django.shortcuts import render
from django.views.generic import ListView, DetailView

from content.models import Movie


class ContentListView(ListView):
    model = Movie


class ContentDetailView(DetailView):
    model = Movie

def home(request):
    return render(request, 'content/home.html')