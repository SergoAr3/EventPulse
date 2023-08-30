import requests
from pages.models import Article, Event
from django.utils import timezone
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def save_latestNews_to_database():
    res = requests.get(
        'https://newsdata.io/api/1/news?&apikey=pub_26805043ee630412dba592e779a90c4e17f20&domain=lenta')
    res.raise_for_status()
    data = res.json()
    for article in data['results']:
        if article['description']:
            title = article['title']
            content = article['content']
            description = article['description']
            source = article['link']
            date_published = timezone.now()
            if 'assets' not in article['image_url']:
                image = article['image_url']
            else:
                image = None
            if not Article.objects.filter(title=title).exists():
                try:
                    Article.objects.create(title=title, description=description, content=content, source=source,
                                           date_published=date_published, image=image)
                except Exception as e:
                    print(f"Ошибка при добавлении новости: {e}")

def save_politicNews_to_database():
    res = requests.get(
        'https://newsdata.io/api/1/news?&apikey=pub_26805043ee630412dba592e779a90c4e17f20&category=politics&domain=lenta,mk')
    res.raise_for_status()
    data = res.json()
    for article in data['results']:
        if article['description']:
            title = article['title']
            content = article['content']
            description = article['description']
            source = article['link']
            date_published = timezone.now()
            image = article['image_url']
            if not Article.objects.filter(title=title).exists():
                try:
                    Article.objects.create(title=title, description=description, content=content, source=source,
                                           date_published=date_published, image=image)
                except Exception as e:
                    print(f"Ошибка при добавлении новости: {e}")

def save_sportsNews_to_database():
    res = requests.get(
        'https://newsdata.io/api/1/news?&apikey=pub_26805043ee630412dba592e779a90c4e17f20&category=sports&domain=lenta,mk')
    res.raise_for_status()
    data = res.json()
    for article in data['results']:
        if article['description']:
            title = article['title']
            content = article['content']
            description = article['description']
            source = article['link']
            date_published = timezone.now()
            image = article['image_url']
            if not Article.objects.filter(title=title).exists():
                try:
                    Article.objects.create(title=title, description=description, content=content, source=source,
                                           date_published=date_published, image=image)
                except Exception as e:
                    print(f"Ошибка при добавлении новости: {e}")

def save_sciencesNews_to_database():
    res = requests.get(
        'https://newsdata.io/api/1/news?&apikey=pub_26805043ee630412dba592e779a90c4e17f20&category=science&domain=lenta,mk')
    res.raise_for_status()
    data = res.json()
    for article in data['results']:
        if article['description']:
            title = article['title']
            content = article['content']
            description = article['description']
            source = article['link']
            date_published = timezone.now()
            image = article['image_url']
            if not Article.objects.filter(title=title).exists():
                try:
                    Article.objects.create(title=title, description=description, content=content, source=source,
                                           date_published=date_published, image=image)
                except Exception as e:
                    print(f"Ошибка при добавлении новости: {e}")

def save_entertainmentNews_to_database():
    res = requests.get(
        'https://newsdata.io/api/1/news?&apikey=pub_26805043ee630412dba592e779a90c4e17f20&category=entertainment&domain=lenta,mk')
    res.raise_for_status()
    data = res.json()
    for article in data['results']:
        if article['description']:
            title = article['title']
            content = article['content']
            description = article['description']
            source = article['link']
            date_published = timezone.now()
            image = article['image_url']
            if not Article.objects.filter(title=title).exists():
                try:
                    Article.objects.create(title=title, description=description, content=content, source=source,
                                           date_published=date_published, image=image)
                except Exception as e:
                    print(f"Ошибка при добавлении новости: {e}")


def save_events_to_database():
    res = requests.get(
        'https://kudago.com/public-api/v1.4/events/?fields=title,,location,place,price,date,images,body_text&page_size=10')
    data = res.json()
    for event in data['results']:
        title = event['title']
        ...

def get_exchange_rate():
    res = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={os.getenv("EXCHANGE_API_KEY")}')
    res.raise_for_status()
    data = res.json()
    usd = str(data['rates']['RUB'])[:5]

    return usd


def upcoming_events(event):
    now = timezone.now()
    diff = event.date - now
    return diff
