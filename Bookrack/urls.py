from django.conf.urls import url
from . import views
from django.urls import path

# urlpatterns=[
#     url(r'^$',views.MyCar),
# ]

urlpatterns=[
    path('', views.index, name='index'),#浏览书架
    # url(r'^bookrack$',views.index,name='index'),   #浏览书架
    url(r'^add/(?P<gid>[0-9]+)$',views.add,name='add'),   #加入书架
    url(r'^clear', views.clear, name='clear'),  # 清空书架
    url(r'^del/(?P<gid>[0-9]+)$',views.delete,name='delete'),#删除书籍
]