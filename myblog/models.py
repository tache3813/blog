from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

SITE_NAME = "Site Name"
PAGE_HEADING = "Page Heading"
PAGE_DESCRIPTION = "Page Description"
AUTHOR_NAME = "Author Name"
AUTHOR_PROFILE = "Author Profile"

class Category(models.Model):
  """記事のカテゴリ"""
  name = models.CharField('CategoryTag', max_length=255)
  created_at = models.DateTimeField('CreatedAt', default=timezone.now)

  def __str__(self):
    return self.name


class Post(models.Model):
  """blogの記事"""
  title = models.CharField('PostTitle', max_length=255)
  text = MarkdownxField('PostContent', help_text='Writing in Markdown')
  created_at = models.DateTimeField('PublishedAt', default=timezone.now)
  category = models.ForeignKey(Category, verbose_name='PostCategory', on_delete=models.PROTECT)
  outline = models.TextField('Outline', blank=True)
  is_public = models.BooleanField('is Public?', default=True)

  def __str__(self):
    return self.title

  def text_to_markdown(self):
    return markdownify(self.text)


class Comment(models.Model):
  """記事のコメント"""
  name = models.CharField('Your name', max_length=30, default="No name")
  text = models.TextField('Comment')
  post = models.ForeignKey(Post, verbose_name="", on_delete=models.PROTECT)
  created_at = models.DateTimeField('PostedAt', default=timezone.now)

  def __str__(self):
    return self.text[:10]


class Description(models.Model):
  """サイトの詳細情報"""
  site = models.OneToOneField(Site, verbose_name='Site', on_delete=models.PROTECT)
  site_name = models.CharField('SiteName', max_length=255, default=SITE_NAME)
  page_heading = models.TextField('PageHeading', max_length=255, default=PAGE_HEADING)
  page_description = models.TextField('PageDescription', max_length=255, default=PAGE_DESCRIPTION)
  author_profile = MarkdownxField('AuthorProfile', default=AUTHOR_PROFILE)

  def __str__(self):
    return self.site_name

  def text_to_markdown(self):
    return markdownify(self.author_profile)
