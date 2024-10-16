from django.urls import path,include
from . import views

urlpatterns = [
    path('', include("appsecundaria.urls")),
    path("",views.index_vista,name="index_vista")
]
