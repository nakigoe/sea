from turtle import title
from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='ファイル選択して下さい')