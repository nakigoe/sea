from django.urls import path
from . views import my_view  #pages are functions, import them from views.py; dot means the same directory

urlpatterns = [
    path('', my_view, name='my-view') #which function corresponds with which address
]
