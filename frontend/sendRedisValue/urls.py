from django.urls import path
from . import views

#urlConf
urlpatterns = [
    path('',views.calculatorHandler),
    path('1',views.getHandler)  
]