# Generated by Django 4.2.3 on 2023-07-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_article_time_since_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
