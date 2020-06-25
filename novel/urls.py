from django.urls import path
from . import views
from django.views.static import serve
app_name='bookinfo'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:novel_Id>/book/',views.book,name='book'),
    # path('<int:novel_Id>/bookrack/',views.bookrack,name='bookrack'),
    path('<int:novel_Id>/type/<page>',views.type,name='type'),
    path('<int:novel_Id>/<int:chart_Id>/content/',views.content,name='content'),
]