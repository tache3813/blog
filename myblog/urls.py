from django.urls import path
from . import views #相対インポート

app_name = 'myblog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
