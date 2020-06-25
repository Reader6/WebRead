from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Novels
from .models import Chart
from .models import Types
from django.http import HttpResponse,HttpResponseRedirect
import random

from django.core.paginator import Paginator,PageNotAnInteger,InvalidPage,EmptyPage
# from djurls.settings import BASE_DIR
# from novel.models import Novels


# Create your views here. 
def index(request):
    recommend_list=Novels.objects.all()[:6];
    request.session['name']='hello'
    recommend_list1 = Novels.objects.all()[7:16];
    recommend_type=Novels.objects.all()[:1]
    recommend_text=random.choice(recommend_list)
    recommend_text1 = random.choice(recommend_list1)
    recommend_newBook=Novels.objects.all().order_by('novel_pv') [:6];
    newCharts=Chart.objects.all()[:20];
    # kw = request.GET.get('kw')
    # if kw:
    #     # 根据关键字模糊搜索
    #     recommend_list = recommend_list.filter(novel_name__contains=kw)
    context = loadinfo(request)
    context={
            'title':'书城',
            'recommend_list':recommend_list,
             'recommend_list1': recommend_list1,
            'recommend_type':recommend_type,
            'recommend_text':recommend_text,
            'recommend_text1': recommend_text1,
            'recommend_newBook':recommend_newBook,
            'newCharts':newCharts,  
    }
    context['types'] = Types.objects.all()
    return render(request,'novel/index.html',context);

def loadinfo(request):
    context={}
    context['types']=Types.objects.all()
    return context

def type(request,novel_Id,page=1):
    novels = get_object_or_404(Novels, pk=novel_Id);
    charts = Chart.objects.filter(novel=novels)
    context=loadinfo(request)
    recommend_list=Novels.objects
    #根据条件筛选小说类型
    tid=request.GET.get('tid',None)
    if tid:
        #根据类型id筛选
        recommend_list=recommend_list.filter(novel_type=tid)

    kw=request.GET.get('kw')
    if kw:
        #根据关键字模糊搜索
        recommend_list=recommend_list.filter(novel_name__contains=kw)

    #若不存在获取所有
    recommend_list=recommend_list.all()
    paginator = Paginator(recommend_list, per_page=10)
    try:
        recommend_list = paginator.page(page)  # 获取指定页的小说记录
        print("当前页的文章信息：", recommend_list.object_list)

    except PageNotAnInteger:
        recommend_list = paginator.page(1)
    except EmptyPage:
        recommend_list = paginator.page(paginator.num_pages)
    except InvalidPage:
        raise Http404("请求的页数不存在")
    context={
        'recommend_list':recommend_list
    }
    if recommend_list.paginator.num_pages >= 13:
        ifEllipsis = 1
        range1 = range(1, 13)
        range2 = range(1, 15)
        range3 = range(1, 14)
        lastButOne = recommend_list.paginator.num_pages - 1
    else:
        ifEllipsis = 0
    context['paginator']=paginator
    context['types'] = Types.objects.all()
    # img=IMG.img_freqency
    return render(request, 'novel/Welcome.html', context);

def book(request,novel_Id):
        novels=get_object_or_404(Novels,pk=novel_Id);
        charts=Chart.objects.filter(novel=novels);
        img=Novels.objects.all()
        # img=IMG.img_freqency
        # print('novel:',novels.novel_freqency);
        # print(charst)
        return render(request,'novel/book.html',{'novel':novels,
        'charts':charts,'img':img
        });

def content(request,novel_Id,chart_Id): 
        novels=get_object_or_404(Novels,pk=novel_Id);
        chart=Chart.objects.filter(novel=novels)[chart_Id]
        return render(request,'novel/content.html',{'chart':chart,
        });

# def bookrack(request,novel_Id):
#     novels = get_object_or_404(Novels, pk=novel_Id);
#     charts = Chart.objects.filter(novel=novels);
#     return render(request, 'novel/bookrack.html', {'novel': novels,
#      'charts': charts, });


#
# def lists(request,page=1):
#     context=loadinfo(request)
#     novel=Novels.objects.all()
#
#     #分页
#     paginator=Paginator(novel,per_page=10)
#     try:
#         novel=paginator.page(page)  #获取指定页的小说记录
#         print("当前页的商品信息：",novel.object_list)
#
#     except PageNotAnInteger:
#         novel=paginator.page(1)
#     except EmptyPage:
#         novel=paginator.page(paginator.num_pages)
#     except InvalidPage:
#         raise Http404("请求的页数不存在")
#     context = {
#         'novel': novel
#     }
#     return render(request,'novel/Welcome.html',context=context)


# def hello(request,novel_Id):
#         novels = get_object_or_404(Novels, pk=novel_Id);
#         Novels.objects.filter(novel=novels)
#         img = Novels.objects.all()
#         #print(img)
#         return render(request, 'novel/book.html',{'img':img})


# def ProductList(request):
#     return HttpResponse("TEST")
# #
# def ProductDetails(request,IdNumber):
#     if request.method=='POST':
#         if 'AddCar' in request.POST:
#             InputCar=Novels.objects.create(ProductID=request.POST['Novels.novel_Id'][0:4],
#                                            ProductName=request.POST['Novels.novel_name'])
#         InputCar.save()
#         return HttpResponseRedirect('/ProductList/%s/' %str(request.POST['ProductID']+'A'))
#     else:
#         return HttpResponseRedirect('/MyCar/')



