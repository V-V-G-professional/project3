from django.db.models import Count
from django.core.cache import cache

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},

]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('animals'))
            cache.set('cats', cats, 60)

        context['menu'] = menu
        context['cats'] = cats
        return context