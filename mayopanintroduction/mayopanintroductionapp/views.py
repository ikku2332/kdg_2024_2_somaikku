from django.shortcuts import render
from django.views.generic import ListView
from .models import ExplanationModel

# Create your views here.
class ListMayopanintroductionView(ListView):
    template_name = 'mayopanintroductionapp/index.html'
    model = ExplanationModel
class ListMayopansynopsisView(ListView):
    template_name = 'mayopanintroductionapp/indexsynopsis.html'
    model = ExplanationModel
class ListMayopancharacterView(ListView):
    template_name = 'mayopanintroductionapp/indexcharacter.html'
    model = ExplanationModel