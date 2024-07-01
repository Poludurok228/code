from django.shortcuts import render
from .models import News


def index(request):
    news = News.objects.all()
    return render(request, 'web_app/home.html', {'news': news})
