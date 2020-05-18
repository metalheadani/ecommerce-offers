from django.shortcuts import render, get_object_or_404
from .models import Offer

from django.urls import reverse

def offers(request, slug):
	template_name = 'userview/home.html'
	offer = get_object_or_404(Offer, slug=slug)
	context = {'offer': offer}
	return render(request, template_name, context)

