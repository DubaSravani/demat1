from django.shortcuts import render
from .forms import supermarket

def market(request):
    form=supermarket()
    if form.is_valid():
        menu=form.GET.get('food_menu')
        print(menu)
    return render(request,"market.html",{"form":form})

# Create your views here.
