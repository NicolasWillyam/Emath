from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('contest/', views.contest , name="contest"),
    path('problems/', views.problems , name="problems"),
    path('submissions/', views.submissions , name="submissions"),
    path('login/', views.login , name="login"),

]
