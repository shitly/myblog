import os

###
from os.path import dirname, abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys
sys.path.insert(0, PROJECT_DIR)
os.environ["DJANGO_SETTINGS_MODULE"] = "minicms.settings"

import django
django.setup()

from datetime import datetime as dt
from numpy.random import randint

from blog.models import LanMu, Column, FrendLink

def push_lm_and_columns():    
    tags = []

    temp = {}
    temp.setdefault("简生活", ["简单趣事", "游戏人生", "小经历", "感悟"])
    temp.setdefault("Web开发", ["Django", "Python_web", "html/css", "JavaScript", "Apache", "OS"])
    temp.setdefault("游戏开发", ["C++", "DirectX", "OpenGL", "引擎相关", "游戏设计"])
    temp.setdefault("数据挖掘", ["竞赛相关", "趣味课题", "开源框架", "ML", "DL&NLP"])
    temp.setdefault("Web安全", [ "抓包相关", "白帽黑客", "入侵操作", "数据库安全", "防护设计"])
    
    for lanmu in temp.keys():
        lm = LanMu.objects.create(lanmu=lanmu)

        for column in temp[lanmu]:
            Column.objects.create(
                lanmu=lm,
                name = column,
                intro = "描述："+column,
            )
    print("写入结束")

push_lm_and_columns()

def push_frendlink():
    temp = {}
    temp.setdefault("半仙世界", "http://www.aljs.pw")
    temp.setdefault("CSDN博客", "https://blog.csdn.net/actanble")
    temp.setdefault("我的github", "https://github.com/actanble")
    temp.setdefault("我的kaggle", "https://kaggle.com/actanble")
    temp.setdefault("我的cnblogs", "https://cnblogs.com/actanble")
    temp.setdefault("知乎", "https://www.zhihu.com/people/actanble/answers")
    temp.setdefault("设计师杨青", "http://www.yangqq.com" )
    temp.setdefault("OpenCV", "http://opencv.org")
    temp.setdefault("django", "https://django-book.com")
    temp.setdefault("阿里云", "https://aliyun.com")

    for key in temp.keys():
        FrendLink.objects.create(name=key, url=temp[key])
    print("写入结束")

push_frendlink()
    