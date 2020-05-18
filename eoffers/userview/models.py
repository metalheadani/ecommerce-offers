from django.db import models
from django.utils.text import slugify


class Offer(models.Model):
	heading = models.CharField(max_length=200, blank=False, null=False, unique=True)
	subheading = models.CharField(max_length=200, blank=True, null=True)
	image_1 = models.ImageField(upload_to='product_images/', blank=True, null=True)
	image_2 = models.ImageField(upload_to='product_images/', blank=True, null=True)
	image_3 = models.ImageField(upload_to='product_images/', blank=True, null=True)
	offer_details = models.CharField(max_length=250, blank=True, null=True)
	t_and_c = models.CharField(max_length=500, blank=True, null=True)
	offer_link = models.URLField(max_length=250, blank=True, null=True)
	discount = models.CharField(max_length=30, blank=True, null=True)
	coupon_code = models.CharField(max_length=50, blank=True, null=True)
	normal_discount = models.CharField(max_length=30, blank=True, null=True)
	price_trend = models.CharField(max_length=50, blank=True, null=True)
	savings = models.CharField(max_length=30, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	slug = models.SlugField(unique=True, blank=True, null=True)

	def __str__(self):
		return '{}'.format(self.heading)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.heading)
		super(Offer, self).save(*args, **kwargs)

