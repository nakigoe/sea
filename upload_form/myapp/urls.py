from django.urls import path
from . views import list_view  #pages are functions, import them from views.py; dot means the same directory

urlpatterns = [
    path('', list_view, name='list-view') #which function corresponds with which address
]
