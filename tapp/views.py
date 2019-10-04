from django.shortcuts import render_to_response, render
import datetime
from .models import Article
from django.http import HttpResponse

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date': now})

def article_list(request):
	articles = Article.objects.all().order_by('date')
	return render_to_response('article_list.html', {'articles': articles})

def article_details(request, slug):
	# through the slug we find the article
	article = Article.objects.get(slug=slug)
	return render_to_response('article_details.html', {'article': article})