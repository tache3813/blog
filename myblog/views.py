from django.db.models import Q # OR検索
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Post, Category

class IndexView(generic.ListView):
  model = Post

  def get_queryset(self):
    queryset = Post.objects.order_by("-created_at")
    keyword = self.request.GET.get('keyword') #検索フォームの入力内容を取得
    if keyword:
      queryset = queryset.filter(
        Q(title__icontains=keyword)|Q(text__icontains=keyword)
      ) #タイトルに含むか検索or本文に含むか検索（大小区別せず）
    return queryset


class CategoryView(generic.ListView):
  model = Post #カテゴリで絞り込んだ記事の一覧を取得する

  def get_queryset(self):
    category = self.get_object_or_404(Category, pk=self.kwargs['pk'])
    queryset = Post.objects.order_by("-created_at").filter(category=category)
    return queryset

