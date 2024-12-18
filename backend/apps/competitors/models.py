from django.db import models
from django.conf import settings
import os

# Create your models here.
class Location(models.Model):
	city_eng = models.CharField(max_length=100)
	city_ru = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	continent = models.CharField(max_length=100)

	def __str__(self):
		return self.city_eng

class Competitor(models.Model):
	name = models.CharField(max_length=100)
	name_id = models.CharField(max_length=100)
	age = models.PositiveIntegerField(blank=True, null=True)
	city = models.ForeignKey(Location, related_name='competitor',
		on_delete=models.PROTECT)
	updated_at = models.DateTimeField(auto_now=True)
	added_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name_id

class CompetitorDetails(models.Model):
	competitor = models.OneToOneField(Competitor, related_name='details', on_delete=models.CASCADE)
	bio = models.TextField(max_length=1000, blank=True, null=True)
	height = models.CharField(max_length=10, blank=True, null=True)
	work = models.CharField(max_length=255, blank=True, null=True)
	study = models.CharField(max_length=255, blank=True, null=True)
	home = models.CharField(max_length=255, blank=True, null=True)
	looking_for = models.CharField(max_length=255, blank=True, null=True)
	relationship_type = models.CharField(max_length=255, blank=True, null=True)
	pronouns = models.CharField(max_length=255, blank=True, null=True)
	lifestyle = models.TextField(max_length=1000, blank=True, null=True)
	more_about_me = models.TextField(max_length=1000, blank=True, null=True)
	languages = models.TextField(max_length=1000, blank=True, null=True)
	tinder_scrape_time = models.DateTimeField()

class CompetitorImage(models.Model):
	image_hash = models.CharField(max_length=64, unique=True, blank=True, null=True)
	beauty_ai_rate = models.FloatField(null=True, blank=True)
	image_local_path = models.CharField(max_length=255) # Путь для хранения изображений
	image_full_path = models.CharField(max_length=255) # Путь для хранения изображений
	competitor = models.ManyToManyField(Competitor, related_name='images')  # Связь с моделью Person

	def get_path(self):
		# Формируем полный путь
		return os.path.join(settings.MEDIA_URL, self.image_local_path)