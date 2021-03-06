from __future__ import unicode_literals

from django.db import models
import sys  # 1


# Create your models here.
class Post(models.Model):
    reload(sys)  # 2
    sys.setdefaultencoding('utf-8')  # 3
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
