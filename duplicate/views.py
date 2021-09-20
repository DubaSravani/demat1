from django.shortcuts import render
from django.http import HttpResponse
def sravani(request):
    return HttpResponse ("hi i am sravani from app2")
def sravs(request):
    tem="index.html"
    a="i am sravani"
    context={"k":a,"q":"hello sravani app2","s":123456}
    return render(request,tem,context)


# Create your views here.
