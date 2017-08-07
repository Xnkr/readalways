# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
	DEFAULT_ID = 1
	categories = models.CharField(max_length=255)

	def __str__(self):
		return '%s' % (self.categories)

class Genre(models.Model):
	genre = models.CharField(max_length=30)
	def __str__(self):
		return '%s' % (self.genre)

class Book(models.Model):
	book_name = models.CharField(max_length = 255)
	book_author = models.CharField(max_length = 255)
	book_category = models.ForeignKey(Categories, on_delete=models.SET_DEFAULT, default=Categories.DEFAULT_ID)
	book_lender = models.ForeignKey(User, on_delete = models.CASCADE)
	book_genre = models.ManyToManyField(Genre, blank=True)
	book_cover = models.ImageField()
	book_edition = models.CharField(max_length=4)

	def __str__(self):
		return '%s - %s - %s' % (self.book_name,self.book_author,self.book_lender)