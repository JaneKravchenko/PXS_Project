from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.views.generic.detail import DetailView
from app_map.models import WorldBorderl
from.forms import MarketEntryForm


from django.shortcuts import render_to_response

def index(request):
    'Display map'
    return render_to_response('base.html', {
    })

def base(request):


    return


class MyView(DetailView):

    model = WorldBorderl
    form = MarketEntryForm
    template_name = "picture.html"
