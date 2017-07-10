from django.shortcuts import render, HttpResponseRedirect
import re
from .models import Article, Column, LanMu, Comment, FrendLink, SliderPic
# Create your views here.
from minicms.settings import split


def index(request):
    return HttpResponseRedirect("/blog/")


def common_content():
    # 点击排行 6 个; 站长推荐 6 个， 最近6 个， 图文6个。; 标签合集 , 友情链接7个
    i_num = 6
    llph = Article.objects.all().order_by('-see_num')[:i_num]
    news = Article.objects.all().order_by('-pub_date')[:i_num]
    zztj = Article.objects.filter(published=True).order_by('pub_date')[:i_num]
    twtj = llph

    tags = Column.objects.all()
    frend_links = FrendLink.objects.all()

    # 未发布的第一条为hot, 尽量保证300x100大小
    hot = Article.objects.filter(published=False).order_by('-pub_date')[0]

    # 友情链接上方为 topnew
    top_new = Article.objects.filter(set_top=True).order_by('-pub_date')[0]
    if not top_new:
        top_new = Article.objects.filter(published=True).order_by('-see_num')[0]

    return {
        "llph": llph,
        "news": news,
        "zztj": zztj,
        "twtj": twtj,
        "tags": tags,
        "frend_links": frend_links,
        "topnew": top_new,
        "hot": hot,
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
    return split_page(request, tag_id, 1)


def lanmu(request, lm_id):
    return split_page2(request, lm_id, 1)

## 详情页

def detail(request, article_id):
    blog = Article.objects.get(id=int(article_id))

    num = blog.see_num
    Article.objects.filter(id=article_id).update(see_num = num+1)

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


# tag分页
def tag_split_page(split, res_data, tag, page):
    pages = [ int(len(res_data)/split) - 1 if len(res_data) % split == 0
                        else int(len(res_data) / split)][0]
    i_pages = [i+1 for i in range(pages + 1)]  # how many pages need to show in html
    # set the start-end pages_num
    i_page_start = split * (int(page) - 1)
    if i_page_start + split-1 < len(res_data):
        i_page_end = i_page_start + split
    else:
        i_page_end = len(res_data)
    # first_post and the posts
    urls = ['/blog/tag/'+ tag + "/index_" + str(i) + "/" for i in i_pages]
    return  {
        # 'slug':'focus_page',
        'page': int(page),
        'urls': urls,
        'blogs': res_data[i_page_start:i_page_end],
    }


# 栏目分页
def lanmu_split_page(split, res_data, lm_id, page):
    # 每8个进行分页_len(res_data)为总条目长度; tag为目标标签的id, page为页数
    # split = 8
    # 总共有多少页
    pages = [ int(len(res_data)/split) - 1 if len(res_data) % split == 0
                        else int(len(res_data) / split)][0]
    i_pages = [i+1 for i in range(pages + 1)]  # how many pages need to show in html
    # set the start-end pages_num
    i_page_start = split * (int(page) - 1)
    if i_page_start + split-1 < len(res_data):
        i_page_end = i_page_start + split
    else:
        i_page_end = len(res_data)
    # first_post and the posts

    urls = ['/blog/lanmu/'+ lm_id + "/index_" + str(i) + "/" for i in i_pages]
    return  {
        # 'slug':'focus_page',
        'page': int(page),
        'urls': urls,
        'blogs': res_data[i_page_start:i_page_end]
    }


def split_page(request, tag_id, page):

    lm = Column.objects.get(id=int(tag_id)).lanmu

    gaim = [x for x in Article.objects.all() if x.column.id == int(tag_id)]

    blogs = gaim
    if len(gaim) <1 :
        blogs = Article.objects.all()
    lms = LanMu.objects.all()

    return render(request, "blog/page.html", {
        "blogs": tag_split_page(split, blogs, tag_id, page)['blogs'],
        "lms" : lms,
        "right": common_content(),
        "tag": Column.objects.get(id=int(tag_id)),
        "lm": lm,
        "split_page": tag_split_page(split, blogs , tag_id, page),
    })

    # 栏目分页
def split_page2(request, lm_id, page):
    tags = [tag for tag in Column.objects.all() if tag.lanmu.id == int(lm_id)]
    ids = [tag.id for tag in tags]
    blogs = [x for x in Article.objects.all() if x.column.id in ids]

    if len(blogs) < 1:
        blogs = blogs = [Article.objects.all()[0] for i in range(18)]
    return render(request, "blog/page.html", {
        "blogs": lanmu_split_page(split, blogs, lm_id, page)['blogs'],
        "lms" : LanMu.objects.all(),
        "right": common_content(),
        "tags": tags,
        "lm": LanMu.objects.get(id=int(lm_id)),
        "split_page": lanmu_split_page(split, blogs, lm_id, page),
    })


