from django.urls import path
from . import views

app_name = 'userview'

urlpatterns = [
	path('<str:slug>', views.offers, name='offershome'),
]

