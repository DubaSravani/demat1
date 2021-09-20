from django.shortcuts import render
from django.http import HttpResponse
def bye(request):
    return HttpResponse ("<h2>bye friends</h2>")
def sravs3(request):
        tem="home.html"
        b="i am sravani"
        context={"k":b,"q":"hello sravani app3","s":123456}
        return render(request,tem,context)
def candy(request):
    s={"key":5,"key1":6}
    return render(request,"insta.html",{"z":s})


# Create your views here.
