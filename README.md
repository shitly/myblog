# 说明
本项目由 `Django==1.10.9` + `py==python3.5.2` 搭建.

项目地址 www.aljs.pw

## 数据初始化注意事项
after `python3 manage.py migrate` ,  `python3 manage.py makemigrations`
只能执行一次下面的指令 ** python3 push_data.py ** 


## 关于 RSS 部分
搜索栏目的时间选定 CSS 乱了, 可以手动安装 YYYY-MM-DD 进行搜索。


## 运行步骤
mycli -uroot -p112233.. 
- CREATE DATABASE `blog` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;


python3 manage.py migrate
python3 manage.py makemigrations
可有\ python3 manage.py migrate
可有\ python3 manage.py makemigrations

 - 无数据库下
python3 blog\push_data.py
python3 manage.py createsuperuser
    接着去后台添加即可。
 - **有数据库**
 source minicms_dump.sql



