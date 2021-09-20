from app3 import views
from django.urls import path
urlpatterns=[
path('hihello/',views.bye,name='bye friends'),
path('sravs/',views.sravs3,name='joker'),
path('candy/',views.candy,name='joker')
]
