from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def hello(request):
    return HttpResponse("hello all from app1")
def hi(request):
    return HttpResponse("hi everyone from app1")
def joker(request):
    t="index.html"
    a="i am sravani"
    context={"k":a,"q":"hello sravani came","s":123456}
    return render(request,t,context)
def tomy(request):
    a=[2,'gh',4,6,7]
    return render(request,"hello.html",{"c":a})
def fly(request):
    a=Book.objects.all()
    return render(request,"home.html",{"data":a})
def flower(request):
    return render(request,"flower.html")
def plant(request):
    return render(request,"plant.html")
def root(request):
    name=request.GET.get('name')
    num1=int(request.GET.get('number1'))
    num2=int(request.GET.get('number2'))
    print(name)
    print(num1)
    print(num2)
    sum=num1+num2
    return render(request,"root.html",{'sum':sum,"n":name})




# Create your views here.
