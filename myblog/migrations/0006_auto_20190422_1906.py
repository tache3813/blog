# Generated by Django 2.1.5 on 2019-04-22 10:06

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20190422_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='author_name',
        ),
        migrations.AlterField(
            model_name='description',
            name='author_profile',
            field=markdownx.models.MarkdownxField(default='Author Profile', verbose_name='AuthorProfile'),
        ),
    ]
