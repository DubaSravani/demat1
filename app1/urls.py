from app1 import views
from django.urls import path

urlpatterns=[
path('hello/',views.hello,name='hello'),
path('hi/',views.hi,name='hi'),
path('joker/',views.joker,name='joker'),
path('tom/',views.tomy,name='joker'),
path('fly/',views.fly,name='fly'),
path('flower/',views.flower,name='flow'),
path('plant/',views.plant,name='plant'),
path('root/',views.root,name='root')
]
