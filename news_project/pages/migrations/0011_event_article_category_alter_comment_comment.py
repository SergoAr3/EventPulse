# Generated by Django 4.2.3 on 2023-07-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('address', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='pages/events/')),
                ('source', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='General', max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
    ]