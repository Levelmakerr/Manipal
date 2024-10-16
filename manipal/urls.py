from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('',views.index),
    path('page',views.page,name='page'),
    path('api/locations/', LocationList.as_view(), name='location-list'),
    path('api/specialities/', SpecialityList.as_view(), name='speciality-list'),
]
