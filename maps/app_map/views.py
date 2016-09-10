from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.views.generic.detail import DetailView
from app_map.models import WorldBorderl

from django.shortcuts import render_to_response

def index(request):
    'Display map'
    return render_to_response('picture.html', {
    })

class MyView(DetailView):

    model = WorldBorderl
    template_name = "picture.html"
