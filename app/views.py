from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.http import HttpResponse
def djforms(request):
    SFO=studentform()
    d={'SFO':SFO}

    if request.method=='POST':
        SFDO=studentform(request.POST)
        if SFDO.is_valid():
            sname=SFDO.cleaned_data['sname']
            return HttpResponse(sname)
        else:
            return HttpResponse ('invalid data')  
    return render(request,'djforms.html',d)            