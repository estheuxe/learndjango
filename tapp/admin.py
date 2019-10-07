from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','date')
	search_fields = ('title','date')

admin.site.register(Article, ArticleAdmin)