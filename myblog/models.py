from django.db import models
from django.utils import timezone

class Category(models.Model):
  """記事のカテゴリ"""
  name = models.CharField('カテゴリ名', max_length=255)
  created_at = models.DateTimeField('作成日', default=timezone.now)

  def __str__(self):
    return self.name

class Post(models.Model):
  """blogの記事"""
  title = models.CharField('タイトル', max_length=255)
  text = models.TextField('本文')
  created_at = models.DateTimeField('作成日', default=timezone.now)
  category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
  #author = models.CharField('User.author', max_length=20)

  def __str__(self):
    return self.title
