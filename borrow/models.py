# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from lend.models import Book

def approved_default():
	return None

# Create your models here.
class BookRequest(models.Model):

	request_sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name="sender")
	book_request = models.ForeignKey(Book, on_delete = models.CASCADE)
	request_receiver = models.ForeignKey(User, on_delete= models.CASCADE, related_name="receiver")
	approved = models.NullBooleanField(default=approved_default)

	def __str__(self):
		return "{}, {} -> {} - approved? {}".format(self.request_sender,self.book_request.book_name,self.request_receiver,self.approved)