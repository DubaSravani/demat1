from app2 import views
from django.urls import path
urlpatterns=[
path('hi/',views.sravani,name='hello from app2'),
path('sravs/',views.sravs,name='joker')
]
