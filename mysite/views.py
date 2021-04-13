from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
	myname = "peggy"
	lotto_numbers = [random.randint(1, 42) for _ in range(6)]

	return render(request, 'index.html', locals())

