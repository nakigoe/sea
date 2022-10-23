from django.db import models
#from django.utils import timezone

class Document(models.Model):
    docfile = models.FileField(upload_to='tosend/', max_length=128) #/documents/%Y/%m/%d
    # time_picked = models.DateTimeField(default=timezone.now)
    # is_sent = models.BooleanField(default=False)
    # time_sent = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return "%s %s %s"%(self.is_sent, self.time_picked, self.docfile) #the record is deleted on send, therefore time_sent is not included in this database review
    # @property
    # def filesize(self):
    #     value = self.docfile.size
    #     if value < 512000:
    #         value = value / 1024.0
    #         ext = 'KB'
    #     elif value < 4194304000:
    #         value = value / 1048576.0
    #         ext = 'MB'
    #     else:
    #         value = value / 1073741824.0
    #         ext = 'GB'
    #     return '%s %s' % (str(round(value, 2)), ext)
    # @property
    # def delete(self, using=None, keep_parents=False):
    #     self.docfile.delete()
    #     super().delete()

    # @property
    # def get_url(self):
    #     if self.docfile and hasattr(self.docfile, 'url'):
    #         return self.docfile.url
    #     else:
    #         return "/static/assembly.png"