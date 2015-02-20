from django.db import models


# Create your models here.
class Store(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    category = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='stores')

    class Meta:
        ordering = ('created',)