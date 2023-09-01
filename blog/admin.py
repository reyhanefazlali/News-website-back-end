from django.contrib import admin
from blog.models import News , Category , Comment


class NewsAdmin(admin.ModelAdmin):
    list_display=['title','created_time','Active']
    search_fields=['title','content']
    list_filter=('Active','newswriter')
    date_hierarchy='updated_time'
    list_display_links=('title','created_time')
    

class CommentAdmin(admin.ModelAdmin):
    list_display=['name','Active','created_time']
    search_fields=['name','post']
    list_filter=('Active',)
    
    

admin.site.register(News,NewsAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
