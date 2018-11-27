# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'data': ['test', '1111', '2222',],
        'data2': ['test2', '2222', '3333',],
        'data3': '1111111 2222222\n333333',
        'data4': '800-COLL444ECE',
        'data5': True,
    }
    return render(request, 'course/index.html', context)

def index2(request, year):
    context = {
        'data11': year
    }
    return render(request, 'course/index.html', context)
