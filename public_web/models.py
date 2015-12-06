from __future__ import unicode_literals

from django.db import models

# Create your models here.



class WebContent(models.Model):
    type = models.TextField(null=False)
    content = models.TextField()
