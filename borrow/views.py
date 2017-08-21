# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from lend import models
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
	string = "hello"
	books = models.Book.objects.all()
	template_name = 'borrow/index.html'
	# return HttpResponse(string)
	context = {
		'name': request.user.username,
		'books': books,
	}
	return render(request, template_name, context)

@login_required
def details(request,book_id):
	book = get_object_or_404(models.Book, id=book_id)
	errors = ""
	context = {
		'book':book,
		'user':request.user,
		'errors': errors,
	}
	template_name = 'borrow/details.html'
	return render(request, template_name, context )