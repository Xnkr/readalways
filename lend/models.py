# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
from django.urls import reverse
from django.utils.deconstruct import deconstructible

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

# Create your models here.

class Category(models.Model):
	DEFAULT_ID = 1
	category_name = models.CharField(max_length=255, unique = True)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return '%s' % (self.category_name)


class Genre(models.Model):
	genre = models.CharField(max_length=30, unique = True)
	def __str__(self):
		return '%s' % (self.genre)

class Book(models.Model):
	class Meta:
		verbose_name_plural = "Books"

	path_and_rename = PathAndRename("covers/") 
	
	book_name = models.CharField(max_length = 255)
	book_author = models.CharField(max_length = 255)
	book_category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=Category.DEFAULT_ID)
	book_lender = models.ForeignKey(User, on_delete = models.CASCADE)
	book_genre = models.ManyToManyField(Genre, blank=True)
	book_cover = models.ImageField(
        upload_to=path_and_rename,
        null=False,
        blank=False,
        editable=True,
        help_text="Book Cover",
        verbose_name="Book Cover"
    )
	book_edition = models.CharField(max_length=4)
	book_borrowable = models.BooleanField(default=True)

	def __str__(self):
		return '%s - %s - %s' % (self.book_name,self.book_author,self.book_lender)

	def get_absolute_url(self):
		return reverse('lend:lend_home')