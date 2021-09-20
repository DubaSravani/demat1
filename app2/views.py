#from django.shortcuts import render
#from django.http import HttpResponse
#def sravani(request):
#    return HttpResponse ("hi i am sravani from app2")
#def sravs(request):
#    tem="index.html"
#    a="i am sravani"
#    context={"k":a,"q":"hello sravani app2","s":123456}
#    return render(request,tem,context)
from django.shortcuts import render
from .models import *

def insta(request):
    a=Insta.objects.all()
    b=Insta.objects.get(id=2)
    c=Insta.objects.get(id=5)
    d=Insta.objects.filter(place="chennai")
    return render(request,"insta.html",{"a":a,"b":b,"c":c,"d":d})
# Create your views here.

# Create your views here.
