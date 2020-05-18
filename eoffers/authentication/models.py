from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
	email = models.CharField(max_length=50,unique=True, blank=False, null=False)
	mobile = models.CharField(max_length=10,null=True,blank=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '{}'.format(self.username)


