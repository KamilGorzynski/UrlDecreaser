from django.db import models


class UrlObject(models.Model):
    link = models.URLField()
    shortcut = models.CharField(max_length=10, default='default_link')

    def __str__(self):
        return self.link
