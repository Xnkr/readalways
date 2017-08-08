# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
	string = "hello"
	# return HttpResponse(string)
	return render(request, 'lend/index.html', {'name' : request.user.username })

