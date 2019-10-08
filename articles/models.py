from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField(max_length=100, verbose_name='Tit-le hehe')
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField('Your image',blank=True,default='default.png')
	author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50] + '...'

# verbose_name or positional in 1 argument