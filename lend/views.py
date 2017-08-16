# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from . import models
# Create your views here.

IMAGE_FILE_TYPES = ['jpg','png','jpeg']

class BookForm(forms.ModelForm):
	class Meta:
		model = models.Book
		fields = ['book_name','book_author','book_category','book_genre','book_cover']


@login_required
def home(request):
	template_name = 'lend/index.html'
	books = models.Book.objects.filter(book_lender=request.user.pk)
	context = {
		'name': request.user,
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
        return redirect('lend:lend_home')
    context = {
        "form": form,
    }
    return render(request, 'lend/create_book.html', context)

@login_required
def delete_book(request, book_id):
    book = models.Book.objects.get(pk=book_id)
    book.delete()
    books = models.Book.objects.filter(book_lender=request.user.pk)
    context = {
				'name': request.user,
				'books' : models.Book.objects.filter(book_lender=request.user.pk),
			}
    return render(request, 'lend/index.html', context)

@login_required
def update_book(request,book_id):
	instance = get_object_or_404(models.Book, id=book_id)
	form = BookForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect('lend:lend_home')
	return direct_to_template(request, 'lend/create_book.html', {'form': form})

@login_required
def details(request,book_id):
	book = get_object_or_404(models.Book, id=book_id)
	errors = ""
	if not book.book_lender == request.user:
		errors = "You did not lend this book. Visit the borrower section"
	context = {
		'book':book,
		'user':request.user,
		'errors': errors,
	}
	template_name = 'lend/details.html'
	return render(request, template_name, context )