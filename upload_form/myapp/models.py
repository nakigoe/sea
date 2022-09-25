from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='/home/ec2-user/test/pdf') #/documents/%Y/%m/%d
