from django.urls import path
from . import views  #pages are functions, import them from views.py; 

urlpatterns = [
    path('', views.list_view, name='list-view'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('sendall/', views.send_all, name='send-all'),
    path('cancelall/', views.cancel_all, name='cancel-all'),
]
