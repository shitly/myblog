from django.contrib import admin
from blog.models import LanMu, Comment, Article, Column, SliderPic


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'article_id', 'pub_date', 'content',)


class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title', 'column', 'set_top', 'published', 'pub_date']

    list_editable = [
         'set_top', 'published', 'column'
    ]

    list_display_links = ['title']

    # 发布文章界面
    fieldsets = [
        (None, {
            'fields': ('pic', 'title', 'summary', 'content', 'column', 'pub_date')
        }),
        ('高级设置', {
            'classes':('collapse',),    # 折叠
            # 'classes': ('wide',),  # 展开
            'fields': ('comment_num', 'set_top', 'published', 'see_num')
        }),
        ('补充', {
            'fields': ()
        }),
    ]


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro', "lanmu", "id")

class SliderPicAdmin(admin.ModelAdmin):
    list_display = ['img', 'desc']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(SliderPic, SliderPicAdmin)
