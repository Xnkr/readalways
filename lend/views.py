# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from django.urls import reverse
from . import models
from borrow import models as b_models

from django.contrib import messages
# Create your views here.

IMAGE_FILE_TYPES = ['jpg','png','jpeg']

class BookForm(forms.ModelForm):
	class Meta:
		model = models.Book
		fields = ['book_name','book_author','book_category','book_genre','book_cover','book_edition']


@login_required
def home(request):
	template_name = 'lend/index.html'
	books = models.Book.objects.filter(book_lender=request.user.pk)
	context = {
		'user': request.user,
		'books' : books,
	}
	return render(request, template_name, context)

@login_required
def create_book(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.book_lender = request.user
        book.book_cover = request.FILES['book_cover']
        selected_cat = form.cleaned_data['book_category']
        file_type = book.book_cover.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'book': book,
                'form': form,
                'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
            return render(request, 'lend/create_book.html', context)
        book.save()        
        if form.cleaned_data['book_genre']:
        	book.book_genre = form.cleaned_data['book_genre']
        	book.save()
        return redirect('lend:lend_home')
    context = {
        "form": form,
    }
    return render(request, 'lend/create_book.html', context)

@login_required
def delete_book(request, book_id):
	book = models.Book.objects.get(pk=book_id)
	if book.book_lender == request.user:
		book.delete()
		books = models.Book.objects.filter(book_lender=request.user.pk)
		context = {
		'user': request.user,
		'books' : models.Book.objects.filter(book_lender=request.user.pk),
		}
	else:
		messages.error(request, 'You cannot delete what you did not add.')
		return redirect('lend:lend_home')
	return render(request, 'lend/index.html', context)

@login_required
def update_book(request,book_id):
	instance = get_object_or_404(models.Book, id=book_id)
	if instance.book_lender == request.user:
		form = BookForm(request.POST or None, request.FILES or None, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('lend:lend_home')
		return render(request, 'lend/create_book.html', {'form': form})
	else:
		messages.error(request, 'You cannot edit what you did not add.')
    	return redirect('lend:lend_home')


@login_required
def approve(request,req_id):
	book_requested = get_object_or_404(b_models.BookRequest, id=req_id)
	if not request.user == book_requested.request_receiver:
		messages.error(request, 'That request was not yours to approve')
	else:
		book_requested.approved = True
		book_requested.save()
		book = book_requested.book_request
		book.book_borrowable = False
		book.save()
		messages.success(request, 'Request has been approved. Your E-Mail is now visible to the requester.')
	return redirect('inbox')

@login_required
def reject(request,req_id):
	book_requested = get_object_or_404(b_models.BookRequest, id=req_id)
	if not request.user == book_requested.request_receiver:
		messages.error(request, 'That request was not yours to reject')
	else:
		book_requested.approved = False
		book_requested.save()
		book = book_requested.book_request
		book.book_borrowable = True
		book.save()
		messages.success(request, 'Request has been rejected.')
	return redirect('inbox')