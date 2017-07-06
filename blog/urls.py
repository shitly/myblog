from django.conf.urls import url
from blog import views
app_name = 'blog'
urlpatterns = [

    url(r'^$', views.homepage, name='index'),

    ## 二级页面
    # 栏目组合页面
    url(r'^lanmu/(?P<lm_id>[0-9]+)/$', views.lanmu, name='blog_lanmu'),
    # 分类的标签页面 - tag=column
    # 
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.page, name='blog_page'),
    
    # 详情页页面
    url(r'^detail/(?P<article_id>[0-9]+)/$', views.detail, name='blog_detail'),
    
    # 
    url(r'^aboutme/$', views.about_me, name='info_page'),
    
    # RSS
    url(r'^rss/$', views.rss, name='RSS'),

]