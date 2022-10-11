from django.db import models
from django.utils import timezone

class Document(models.Model):
    docfile = models.FileField(upload_to='tosend/', max_length=128) #/documents/%Y/%m/%d
    # time_picked = models.DateTimeField(default=timezone.now)
    # is_sent = models.BooleanField(default=False)
    # time_sent = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return "%s %s %s"%(self.is_sent, self.time_picked, self.docfile) #the record is deleted on send, therefore time_sent is not included in this database review