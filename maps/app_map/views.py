# coding=utf-8
from django.template.context import RequestContext

from django.contrib.gis.measure import D
from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.views.generic.detail import DetailView

from .models import Cnotozymi
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.contrib.gis.geos import GEOSGeometry, Polygon
from django.template import Context, Template
import re
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse


class Home(ListView):
    template_name = "base.html"
    model = Cnotozymi
    context_object_name = 'cnotozymi'




def proseccing_request(request):
    try:
       if request.GET.items()!=[]:
          req = str(request.GET.items()[0])
          search = re.findall('[\d]+\.[\d]+', str(req))
          sort_point_x = float(search[0])

          sort_point_y = float(search[1])


          print request.GET.items()
          queryset = Cnotozymi.objects.filter(
        geom__distance_lte=(GEOSGeometry('POINT(' + str(sort_point_x) + ' ' + str(sort_point_y) + ')'), D(m=0)))

          return render_to_response("project.html", {"object": queryset[0]})
    except:
        return render_to_response("project.html", {"notobject": "Не знайдено"})







class Project(ListView):
    template_name = "project.html"
    model = Cnotozymi
    context_object_name = 'cnotozymi'




def project(request):
    cnotozymi = Cnotozymi.objects.all()
    context = {
        'cnotozymi': cnotozymi
    }

    return render(request, 'project.html', context)


def help(request):
    return render_to_response('help.html', {})

def temp(request):
    return render_to_response('temp.html', {})


def index(request):
    return render_to_response('base.html', {})


def base(request):
    return


def statistic(request):
    if request.GET.items() != []:
        req = str(request.GET.items()[0])
        search = re.findall('[\d]+\.[\d]+', str(req))

        tuple_of_coordinates = []
        print search
        for i in range(0,len(search)-1,2):
            tuple_of_coordinates.append((float(search[i]), float(search[i+1])))
        queryset = Cnotozymi.objects.filter(
            geom__distance_lte=(Polygon(tuple(tuple_of_coordinates)), D(m=0)))


        pl = sum(map(lambda i: queryset[i].s_ga, range(len(queryset))))
        type_fields =map(lambda i: queryset[i].crop, range(len(queryset)))

        sum_harvest = sum(map(lambda i: queryset[i].harvest, range(len(queryset))))
        return render_to_response("statistic.html", {"count": queryset.count(), "pl": pl, "harvest": sum_harvest})