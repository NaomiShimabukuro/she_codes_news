# Generated by Django 4.2.2 on 2023-12-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsstory',
            name='image',
        ),
        migrations.AddField(
            model_name='newsstory',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='newsstory',
            name='news_image',
            field=models.URLField(blank=True),
        ),
    ]
