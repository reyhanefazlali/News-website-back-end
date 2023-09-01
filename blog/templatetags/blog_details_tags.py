from django import template
from ..models import News , Category 

register=template.Library()

@register.inclusion_tag('blog/recentnews.html')
def recentnews():
    news=News.objects.filter(Active=1).order_by('-created_time')
    return {'news':news}

@register.inclusion_tag('blog/category.html')
def sidebar_category():
    news=News.objects.filter(Active=1)
    categories=Category.objects.all()
    Dict={}
    
    for cat in categories:
        Dict[cat]=news.filter(category=cat).count()
        
    return {'Dict':Dict}

@register.inclusion_tag('blog/tag-clouds.html')
def sidebar_tags():
    news=News.objects.filter(Active=1)
    tags=News.tag.all()
    Dict={}
    
    for tagi in tags:
        Dict[tagi]=news.filter(tag=tagi).count()
        
    return {'Dict':Dict}