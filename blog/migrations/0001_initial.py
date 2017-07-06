# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-06 03:11
from __future__ import unicode_literals

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_top', models.BooleanField(default=False, verbose_name='设为置顶')),
                ('pic', models.ImageField(default='uploads/blog/images/default.jpg', upload_to='uploads/blog/images/', verbose_name='文章标头图片535*270')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('summary', models.TextField(default=' ', verbose_name='概要')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('see_num', models.IntegerField(verbose_name='浏览数')),
                ('comment_num', models.IntegerField(default=0)),
                ('published', models.BooleanField(default=True, verbose_name='发布与否')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='column_name')),
                ('intro', models.TextField(default='', verbose_name='introduction')),
            ],
            options={
                'verbose_name': 'column',
                'ordering': ['name'],
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '评论',
            },
        ),
        migrations.CreateModel(
            name='LanMu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lanmu', models.CharField(max_length=256, verbose_name='栏目')),
            ],
            options={
                'verbose_name': '栏目',
            },
        ),
        migrations.CreateModel(
            name='SliderPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='uploads/blog/images/default.jpg', upload_to='', verbose_name='首页图片')),
                ('desc', models.CharField(default='', max_length=222, verbose_name='图片描述')),
            ],
        ),
        migrations.AddField(
            model_name='column',
            name='lanmu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.LanMu', verbose_name='所属栏目'),
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Column', verbose_name='小标签'),
        ),
    ]
