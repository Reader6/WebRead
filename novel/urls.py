from django.urls import path

from . import views
app_name='bookinfo'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:novel_Id>/book/',views.book,name='book'),
    path('<int:novel_Id>/<int:chart_Id>/content/',views.content,name='content'),
]