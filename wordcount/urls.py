
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('countword/',views.count, name='count'),
    path('aboutus/',views.about, name='abouts'),

]