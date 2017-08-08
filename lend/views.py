# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import models
# Create your views here.

@login_required
def home(request):
	template_name = 'lend/index.html'
	books = models.Book.objects.filter(book_lender=request.user.pk)
	context = {
		'name': request.user,
		'books' : books,
	}
	return render(request, template_name, context)

