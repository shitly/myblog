from django.shortcuts import render, HttpResponseRedirect
import re
from .models import Article, Column, LanMu, Comment, FrendLink, SliderPic
# Create your views here.

def index(request):
    return HttpResponseRedirect("/blog/")


def common_content():
    # 点击排行 6 个; 站长推荐 6 个， 最近6 个， 图文6个。; 标签合集 , 友情链接7个
    i_num = 6
    llph = Article.objects.filter(published=True).order_by('-see_num')[:i_num]
    news = Article.objects.filter(published=True).order_by('-pub_date')[:i_num]
    zztj = Article.objects.filter(published=True).order_by('pub_date')[:i_num]
    twtj = Article.objects.filter(published=True).order_by('-pub_date')[:i_num]

    tags = Column.objects.all()
    frend_links = FrendLink.objects.all()

    return {
        "llph": llph,
        "news": news,
        "zztj": zztj,
        "twty": twtj,
        "tags": tags,
        "frend_links": frend_links, 
}

def homepage(request):

    slider_pics = SliderPic.objects.all()[:4]
    blogs = Article.objects.all()[:8]

    return render(request, "blog/homepage.html", {
        "slider_pics": slider_pics,
        "lms": LanMu.objects.all(),
        "blogs": blogs,
        "right": common_content(),

}) 



## 两个二级页
def page(request, tag_id):
    lm = Column.objects.get(id=int(tag_id)).lanmu

    gaim = [x for x in Article.objects.all() if x.column.id == int(tag_id)]
    
    blogs = gaim
    if len(gaim) <1 :
        blogs = [Article.objects.all()[0] for i in range(8)]
    lms = LanMu.objects.all()

    return render(request, "blog/page.html", {
        "blogs": blogs,
        "lms" : lms,
        "right": common_content(),
        "tag": Column.objects.get(id=int(tag_id)),
        "lm": lm,
})


def lanmu(request, lm_id):
    tags = [tag for tag in Column.objects.all() if tag.lanmu.id == int(lm_id)]
    ids = [tag.id for tag in tags]
    blogs = [x for x in Article.objects.all() if x.column.id in ids]

    if len(blogs) < 1:
        blogs = blogs = [Article.objects.all()[0] for i in range(8)]
    return render(request, "blog/page.html", {
        "blogs": blogs,
        "lms" : LanMu.objects.all(),
        "right": common_content(),
        "tags": tags,
        "lm": LanMu.objects.get(id=int(lm_id)),
})

## 详情页

def detail(request, article_id):
    blog = Article.objects.get(id=int(article_id))

    return render(request, "blog/detail.html", {
        "lms": LanMu.objects.all(),
        "blog": blog,
        "right": common_content(),
        })



def about_me(request):
    return HttpResponseRedirect("/") 


from blog.forms import SearchForm
def rss(request):
    
    if request.method == 'GET':
        form = SearchForm(initial={'title_word': "."})
        return render(request, 'blog/rss.html', {
            'form': form,
            "lms" : LanMu.objects.all(),
            "right": common_content(),
        })

    if request.method == 'POST':
        form = SearchForm(request.POST)
        # 探究搜索关键词为空的内容// 搜素全部为 .
        if form.is_valid():

            tag = form.cleaned_data['tag']
            start_date = form.cleaned_data['serach_start']
            end_date = form.cleaned_data['serach_end']
            word = form.cleaned_data['title_word']
            temp_res = Article.objects.all()
            result1 = [x for x in temp_res if x.pub_date.date() > start_date and x.pub_date.date() <= end_date]
            result0 = [x for x in result1 if x.column == tag]
            result = []
            for x in result0:
                if re.match(".*" + word + ".*", x.title):
                    result.append(x)

            return render(request, "blog/rss.html", {
                'form': form,
                "blogs": result,
                "lms" : LanMu.objects.all(),
                "right": common_content(),
            })
        return render(request, 'blog/rss.html', {
            'form': form,
            "lms" : LanMu.objects.all(),
            "right": common_content(),
        })




