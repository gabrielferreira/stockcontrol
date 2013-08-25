# -*- coding: utf-8 -*- 
from django.db import models

# Create your models here.

class Area(models.Model):
	name = models.CharField(u'Nome', max_length=100, unique=True)
	description = models.TextField(u'Descrição', blank=True, null=True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'Área'
		verbose_name_plural = u'Áreas'


class Size(models.Model):
	code = models.CharField(u'Código', max_length=5, unique=True)
	description = models.TextField(u'Descrição', blank=True, null=True)

	def __unicode__(self):
		return self.code

	class Meta:
		verbose_name = u'Tamanho'
		verbose_name_plural = u'Tamanhos'