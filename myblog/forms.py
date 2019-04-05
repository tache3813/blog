from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):

  #特殊メソッドinitのカスタマイズ(bootstarp4に対応するCSSの追加)
  def __init__(self, *args, **kwargs):
    super().__init__(*args, ** kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form_control'

  class Meta:
    model = Comment
    fields = (
      'name',
      'text',
    )
