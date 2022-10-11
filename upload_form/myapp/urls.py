from django.urls import path
from . import views  #pages are functions, import them from views.py; 

urlpatterns = [
    path('', views.list_view, name='list-view'),
    path('sendall/', views.send_all, name='send-all'),
]
