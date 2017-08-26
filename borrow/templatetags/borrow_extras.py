from django import template
from lend.models import Book
from borrow.models import BookRequest
from django.shortcuts import get_object_or_404

register = template.Library()

@register.filter(name='request_check')
def request_check(value,arg): 
	book_id = value
	book = get_object_or_404(Book, id=book_id)
	requested = False
	try:
		requested_book = BookRequest.objects.get(book_request=book,request_sender=arg)
		requested = True
	except BookRequest.DoesNotExist:
		requested = False
	return requested