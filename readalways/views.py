from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from borrow import models as b_models
from lend import models as l_models

def home(request):
	if not request.user.is_authenticated():
		user = "Anonymous"
	else:
		user = request.user
	context = {
		'user':user,
	}
	return render(request,'home/index.html',context)

@login_required
def inbox(request):
	user = request.user
	incoming = b_models.BookRequest.objects.filter(request_receiver=user) 
	outgoing = b_models.BookRequest.objects.filter(request_sender=user)
	context = {
		'user':user,
		'incoming':incoming,
		'outgoing':outgoing,
	}
	return render(request,'home/inbox.html',context)	

