# -*- coding: utf-8 -*-
from django.http import *
from django.shortcuts import render_to_response

def merhaba_dunya(request):
    return render_to_response('merhaba.html')