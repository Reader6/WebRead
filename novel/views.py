from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.shortcuts import render,get_object_or_404
from .models import Novels
from .models import Chart
# from .models import IMG
from django.http import HttpResponse,HttpResponseRedirect
import random
# Create your views here. 
def index(request):
    recommend_list=Novels.objects.all()[:6];
    recommend_list1 = Novels.objects.all()[7:16];
    recommend_text=random.choice(recommend_list)
    recommend_text1 = random.choice(recommend_list1)
    recommend_newBook=Novels.objects.all().order_by('novel_pv') [:6];
    newCharts=Chart.objects.all()[:20];
    context={
            'title':'书城',
            'recommend_list':recommend_list,
             'recommend_list1': recommend_list1,
            'recommend_text':recommend_text,
            'recommend_text1': recommend_text1,
            'recommend_newBook':recommend_newBook,
            'newCharts':newCharts,  
    }
    return render(request,'novel/index.html',context);
def book(request,novel_Id):
        novels=get_object_or_404(Novels,pk=novel_Id);
        charts=Chart.objects.filter(novel=novels);
        
        return render(request,'novel/book.html',{'novel':novels,
        'charts':charts,
        });

def content(request,novel_Id,chart_Id): 
        novels=get_object_or_404(Novels,pk=novel_Id);
        chart=Chart.objects.filter(novel=novels)[chart_Id]
        return render(request,'novel/content.html',{'chart':chart,
        });
