# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from lend import models
from models import BookRequest
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
	books = models.Book.objects.exclude(book_lender=request.user)
	template_name = 'borrow/index.html'
	# return HttpResponse(string)
	context = {
		'user': request.user,
		'books': books,
	}
	return render(request, template_name, context)

@login_required
def details(request,book_id):
	book = get_object_or_404(models.Book, id=book_id)
	errors = ""
	requested = False

	if book.book_lender == request.user:
		errors += "You did lent this book. Visit the lend section"
	else:
		try:
			requested_book = BookRequest.objects.get(book_request=book,request_sender=request.user)
			requested = True
		except BookRequest.DoesNotExist:
			requested = False

		if request.method == "POST":
			book_req = BookRequest(
				request_sender=request.user,
				request_receiver=book.book_lender,
				book_request=book
				)
			book_req.save()
			requested = True
	context = {
		'book':book,
		'user':request.user,
		'errors': errors,
		'requested': requested,
	}
	template_name = 'borrow/details.html'
	return render(request, template_name, context )