from django.shortcuts import render,redirect
from .models import Edubridge
from .forms import EdubridgeForm
def eform(request):
    form=EdubridgeForm()
    if request.method=='POST':
        form=EdubridgeForm(request.POST,request.FIELS)
        if form.is_valid():
            form.save()
            return redirect("eall")
        else:
            return redirect("hello")
    else:
       form=EdubridgeForm()
    return render(request,"eform.html",{"form":form})
        

# Create your views here.
