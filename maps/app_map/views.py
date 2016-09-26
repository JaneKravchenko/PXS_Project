# coding=utf-8
from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.views.generic.detail import DetailView

from .models import Cnotozymi

from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.gis.geos import GEOSGeometry


def home(request):

        cnotozymi = Cnotozymi.objects.get(geom__within = GEOSGeometry('POINT(48.36454 30.69134)', srid=4326))
        context = {
            'cnotozymi': cnotozymi
        }





        return render(request, "base.html", context)


def project(request):
    cnotozymi = Cnotozymi.objects.filter(gid=2)
    context = {
        'cnotozymi': cnotozymi
    }

    return render(request, 'project.html', context)


def help(request):
    return render_to_response('help.html', {})


def index(request):
    return render_to_response('base.html', {})


def base(request):
    return
