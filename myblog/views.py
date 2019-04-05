from django.db.models import Q # OR検索
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Post, Category, Comment
from .forms import CommentCreateForm

class IndexView(generic.ListView):
  model = Post
  paginate_by = 5

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
  paginate_by = 5

  def get_queryset(self):
    category_pk = self.kwargs['pk']
    queryset = Post.objects.order_by("-created_at").filter(category_pk=category_pk)
    return queryset


class DetailView(generic.DetailView):
  model = Post


class CommentView(generic.CreateView):
  model = Comment
  form_class = CommentCreateForm

  # formのvalidationチェックに成功したら呼び出す
  def form_valid(self, form):
    post_pk = self.kwargs['post_pk']
    comment = form.save(commit=False) # まだコメントをDBに保存していない
    comment.post = get_object_or_404(Post, pk=post_pk)
    comment.save()
    return redirect('myblog:detail', pk=post_pk)
