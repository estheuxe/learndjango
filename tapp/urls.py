from django.urls import path
from . import views

# namespace for this view
app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('<slug:slug>/', views.article_details, name='detail'),
]