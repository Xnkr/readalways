# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
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