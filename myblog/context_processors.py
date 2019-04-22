from django.contrib.sites.shortcuts import get_current_site
from .models import Category, Description

def common(request):
    """テンプレートに毎回渡すデータ"""
    site = get_current_site(request)
    mysite, _ = Description.objects.get_or_create(site=site)
    context = {
        'category_list': Category.objects.all(),
        'mysite': mysite,
    }
    return context
