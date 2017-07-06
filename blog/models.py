import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField


# 首页图片
@python_2_unicode_compatible
class SliderPic(models.Model):
    img = models.ImageField("首页图片670x280", default='uploads/blog/images/default.jpg')
    desc = models.CharField("图片描述", max_length=222, default='')


# 栏目
@python_2_unicode_compatible
class LanMu(models.Model):
    lanmu = models.CharField('栏目', max_length=256)

    def __str__(self):
        return self.lanmu

    class Meta:
        verbose_name = '栏目'


# 标签
@python_2_unicode_compatible
class Column(models.Model):
    lanmu = models.ForeignKey(LanMu, blank=True, null=True, verbose_name='所属栏目')
    name = models.CharField('column_name', max_length=256)
    intro = models.TextField('introduction', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'column'
        verbose_name_plural = '标签'
        ordering = ['name']


@python_2_unicode_compatible
class Article(models.Model):
    set_top = models.BooleanField('设为置顶', default=False)
    pic = models.ImageField('文章标头图片245x200', upload_to='uploads/blog/images/',
                            default='uploads/blog/images/default.jpg')
    column = models.ForeignKey(Column, blank=True, null=True, verbose_name='小标签')
    title = models.CharField(verbose_name="标题", max_length=256)
    summary = models.TextField(verbose_name="概要", default=" ")
    content = UEditorField('内容', height=500, width=1200,
        default='', blank=True, imagePath="uploads/images/%(basename)s_%(datetime)s.%(extname)s",
        toolbars='full', filePath='uploads/files/%(basename)s_%(datetime)s.%(extname)s')
    pub_date = models.DateTimeField(verbose_name="发表时间")
    see_num = models.IntegerField(verbose_name="浏览数")
    comment_num = models.IntegerField(default=0)
    published = models.BooleanField("发布与否", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = '文章'


@python_2_unicode_compatible
class Comment(models.Model):
    user = models.ForeignKey(User, null=True)
    article = models.ForeignKey(Article, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'


@python_2_unicode_compatible
class FrendLink(models.Model):
    name = models.CharField("名称描述", max_length = 122)
    url = models.CharField("链接", max_length = 122)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友链'