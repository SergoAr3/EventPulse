from django.shortcuts import render, get_object_or_404
from .models import Article, Event
from .utils import get_exchange_rate, save_latestNews_to_database, upcoming_events


def index(request):
    save_latestNews_to_database()
    latest_articles = Article.objects.order_by('-date_published')[:6]
    selected_city = request.GET.get('city')
    if selected_city:
        events = Event.objects.filter(city=selected_city).order_by('city')
    else:
        events = Event.objects.all()
    latest_events = sorted(events, key=upcoming_events, reverse=False)[:5]
    exchange_rate = get_exchange_rate()

    context = {
        'latest_articles': latest_articles,
        'latest_events': latest_events,
        'exchange_rate': exchange_rate,
    }

    return render(request, 'main.html', context)


def news_detail(request, news_id):
    selected_city = request.GET.get('city')
    if selected_city:
        events = Event.objects.filter(city=selected_city).order_by('city')
    else:
        events = Event.objects.all()
    latest_events = sorted(events, key=upcoming_events, reverse=False)[:5]
    news = get_object_or_404(Article, id=news_id)
    exchange_rate = get_exchange_rate()
    latest_articles = Article.objects.order_by('-date_published')[:4]

    context = {
        'news': news,
        'latest_events': latest_events,
        'exchange_rate': exchange_rate,
        'latest_articles': latest_articles,
    }
    return render(request, 'news_detail.html', context)


def confirmation(request):
    return render(request, 'confirmation.html')
