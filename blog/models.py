#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Bebida(models.Model):
  nombre = models.CharField(max_length=50)
  ingredientes = models.TextField()
  preparacion = models.TextField()

  def __unicode__(self):
      return self.nombre
