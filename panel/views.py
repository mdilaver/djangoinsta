from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
# Create your views here.

@login_required
def yonetim(reqest):
    return render_to_response('registration/index.html', locals())


def login(request):
    if request.GET.get('cikis'):
        logout(request)
        return HttpResponseRedirect('/yonetim')
    if request.POST.get('login'):
        giris_formu = AuthenticationForm(data=request.POST)
        if giris_formu.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            kullanici = authenticate(username=username, password=password)
            if kullanici is not None:
                if kullanici.is_active:
                    login(request, kullanici)
            else:
                giris_formu = AuthenticationForm()
            return render_to_response('registration/index.html', locals(), context_instance=RequestContext(request))
