from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=254)
	text = models.TextField()
	added_at = models.DateTimeField(default=timezone.now)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, related_name='likes_set')
	def __unicode__(self):
		return self.title

class QuestionManager(models.Manager):
	def new(self):
		return self.objects.order_by('added_at').reverse()
	def popular(self):
		return self.objects.order_by('rating').reverse()

class Answer(models.Model):
	title = models.CharField(max_length=254)
	text = models.TextField()
	added_at = models.DateTimeField(default=timezone.now)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
