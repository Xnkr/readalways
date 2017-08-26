# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from lend import models
from models import BookRequest

from django.contrib import messages
from django.db.models import Q
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
	books = models.Book.objects.exclude(book_lender=request.user)
	books = books.filter(book_borrowable=True)
	lenders = books.values_list('book_lender', flat=True).distinct()
	book_by_user = {}
	for c in lenders:
		book_by_user[User.objects.get(id=c).username]=books.filter(book_lender=c)
	requested = False
	if request.method == "POST":
		book_id = request.POST.get("book_id")
		book = get_object_or_404(models.Book, id=book_id)
		book_req = BookRequest(
			request_sender=request.user,
			request_receiver=book.book_lender,
			book_request=book
		)
		book_req.save()
		requested = True
		messages.success(request, 'Your request has been sent. Check your inbox for status.')

	template_name = 'borrow/index.html'
	context = {
		'user': request.user,
		'books': books,
		'book_by_user': book_by_user,		
		'requested': requested,
	}
	return render(request, template_name, context)

@login_required
def fetch_details(request):
	book_id = request.GET.get("book_id")
	book = get_object_or_404(models.Book, id=book_id)
	context = {
	'book':book,
	}
	template_name = 'borrow/detail.html'

	return render(request,template_name,context)

@login_required
def search(request):
	q = request.GET.get('q')
	print q
	results = None
	template_name = 'borrow/results.html'
	if q is not None:
		books = models.Book.objects.exclude(book_lender=request.user)
		books = books.filter(book_borrowable=True)
		results = books.filter(Q( book_name__contains = q ) |
			Q( book_author__contains = q )).order_by('book_name')
		print results
	context = {
		'results':results,
	}
	return render(request, template_name, context)