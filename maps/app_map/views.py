# coding=utf-8
from django.template.context import RequestContext

from django.contrib.gis.measure import D
from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.views.generic.detail import DetailView

from .models import Finalelim
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.contrib.gis.geos import GEOSGeometry, Polygon, LineString, Point
from pyproj import Proj, transform
from collections import Counter

import re
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse


class Home(ListView):
    template_name = "base.html"
    model = Finalelim
    context_object_name = 'cnotozymi'





def proseccing_request(request):
    try:
       if request.GET.items()!=[]:
          req = str(request.GET.items()[0])
          search = re.findall('[\d]+\.[\d]+', str(req))
          sort_point_x = (float(search[0]))
          sort_point_y = (float(search[1]))
          print 1
          inProj = Proj(init='epsg:3857')
          print 2
          outProj = Proj(init='epsg:4326')
          print 3
          list_o =  transform(inProj, outProj, sort_point_x, sort_point_y)
          print 4
          x = list_o[0]
          print x
          y = list_o[1]
          print y
          print request.GET.items()
          pnt = GEOSGeometry('POINT(' + str(x) + ' ' + str(y) + ')')
          print pnt
          queryset = Finalelim.objects.filter(geom__distance_lte = (pnt, D(m=0)))
          print queryset
          return render_to_response("project.html", {"object": queryset[0]})
    except:

        return render_to_response("project.html", {"notobject": "В цій точці інформацію не знайдено."})







class Project(ListView):
    template_name = "project.html"
    model = Finalelim
    context_object_name = 'cnotozymi'




def project(request):
    cnotozymi = Finalelim.objects.all()
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
        if len(search)>7:
            try:
               tuple_of_coordinates = []
               print search
               inProj = Proj(init='epsg:3857')
               outProj = Proj(init='epsg:4326')
               for i in range(0,len(search)-1,2):
                  print 123
                  tuple_of_coordinates.append((transform(inProj, outProj, float(search[i]), float(search[i+1]))))
               queryset = Finalelim.objects.filter(
                geom__contained=(Polygon(tuple(tuple_of_coordinates))))



               pl = sum(map(lambda i: queryset[i].area_ha, range(len(queryset))))
               type_fields =map(lambda i: queryset[i].comment, range(len(queryset)))
               print type_fields[0]
               cnt_crop = Counter(type_fields)
               k = cnt_crop[u'кукурудза']
               sn = cnt_crop[u'соняшник']
               sy = cnt_crop[u'соя']
               ins = cnt_crop[u'інші культури']
               k_q = queryset.filter(comment = "кукурудза")
               sn_q = queryset.filter(comment = "соняшник")
               sy_q = queryset.filter(comment = "соя")
               ins_q = queryset.filter(comment = "інші культури")
               if k >0:
                  pl_k = sum(map(lambda i: k_q[i].area_ha, range(len(k_q))))
               else:
                  pl_k = 0
               if sn > 0:
                  pl_sn = sum(map(lambda i: sn_q[i].area_ha, range(len(sn_q))))
               else:
                  pl_sn = 0
               if sy > 0:
                  pl_sy = sum(map(lambda i: sy_q[i].area_ha, range(len(sy_q))))
               else:
                  pl_sy = 0
               if ins > 0:
                  pl_ins = sum(map(lambda i: ins_q[i].area_ha, range(len(ins_q))))
               else:
                  pl_ins = 0

               count = queryset.count()

               if count >0:
                   return render_to_response("statistic.html", {"count": queryset.count(), "soya_ha": pl_sy, "soya_cnt": sy,
                                                             "son_ha": pl_sn, "son_cnt": sn,
                                                             "k_ha": pl_k, "k_cnt": k,
                                                             "in_ha": pl_ins, "in_cnt": ins,
                                                             "pl" : pl})
            except:
               return render_to_response("statistic.html", {"count": '0', "pl": '0'})


def dist(request):
    req = str(request.GET.items()[0])
    search = re.findall('[\d]+\.[\d]+', str(req))
    tuple_of_coordinates = []

    for i in range(0, len(search) - 1, 2):
        tuple_of_coordinates.append((float(search[i+1]), float(search[i])))
    line = LineString(tuple(tuple_of_coordinates))


    dist = (line.length/1000)/1.6
    return render_to_response("dist.html", {"distance": dist})
