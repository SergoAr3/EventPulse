from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.files.base import ContentFile
import requests


class Article(models.Model):
    title = models.CharField(max_length=500)
    source = models.TextField(max_length=500, blank=True, null=True)
    date_published = models.DateTimeField()
    description = models.TextField(default='')
    content = models.TextField(default='')
    category = models.CharField(max_length=50, default="General")
    image = models.URLField(blank=True, null=True)

    def time_since_published(self):
        if self.date_published:
            now = timezone.now()
            time_diff = now - self.date_published
            if time_diff.days > 0:
                if str(time_diff.days)[-1] in ['2', '3', '4'] and time_diff.days not in [12, 13, 14]:
                    return f"{time_diff.days} дня назад"
                if str(time_diff.days)[-1] == '1' and time_diff.days != 11:
                    return f"{time_diff.days} день назад"
                else:
                    return f"{time_diff.days} дней назад"

            elif time_diff.seconds >= 3600:
                hours = time_diff.seconds // 3600
                if str(hours)[-1] in ['2', '3', '4'] and hours not in [12, 13, 14]:
                    return f"{hours} часа назад"
                if str(hours)[-1] == '1' and hours != 11:
                    return f"{hours} час назад"
                else:
                    return f"{hours} часов назад"

            else:
                minutes = time_diff.seconds // 60
                if minutes == 0:
                    return 'Только что'
                if str(minutes)[-1] in ['2', '3', '4'] and minutes not in [12, 13, 14]:
                    return f"{minutes} минуты назад"
                if str(minutes)[-1] == '1' and minutes != 11:
                    return f"{minutes} минуту назад"
                else:
                    return f"{minutes} минут назад"
        return None

    objects = models.Manager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255)
    comment = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.author_name}: {self.comment}'


class Event(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateTimeField()
    city = models.CharField(max_length=55)
    address = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pages/events/', blank=True, null=True)
    source = models.TextField(blank=True)
    description = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.title
