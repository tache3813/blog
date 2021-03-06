# Generated by Django 2.1.5 on 2019-04-22 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('myblog', '0004_auto_20190422_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='Site Name', max_length=255, verbose_name='SiteName')),
                ('page_heading', models.TextField(default='Page Heading', max_length=255, verbose_name='PageHeading')),
                ('page_description', models.TextField(default='Page Description', max_length=255, verbose_name='PageDescription')),
                ('author_name', models.CharField(default='Author Name', max_length=255, verbose_name='AuthorName')),
                ('author_profile', models.CharField(default='Author Profile', max_length=255, verbose_name='AuthorProfile')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='sites.Site', verbose_name='Site')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='is Public?'),
        ),
    ]
