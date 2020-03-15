from django.db import models

# Create your models here.
class Novels(models.Model):
    novel_Id=models.IntegerField(primary_key=True,);#字段ID
    novel_name=models.CharField(max_length=20); #字段名
    novel_author=models.CharField(max_length=20);#作者名
    novel_pv=models.IntegerField(default=0);#点击量
    novel_img=models.CharField(max_length=500);#封面路径
    novel_type=models.CharField(max_length=20);#小说类型咱
    novel_des=models.CharField(max_length=1000);#小说介绍
    novel_addTime=models.DateTimeField("Date published",auto_now=True);#发表日期
    def __str__ (self):
        return self.novel_name;
class Chart(models.Model):
    novel=models.ForeignKey(Novels,on_delete=models.CASCADE);#章节所属信息
    novel_idx=models.IntegerField();#章节号
    novel_title=models.CharField(max_length=100);#章节标题
    novel_cont=models.TextField(max_length=10000);#章节内容

    class Meta:
        unique_together=(("novel","novel_idx"),)
    def __str__(self):
        return self.novel_title;

class IMG(models.Model):
    name = models.ForeignKey(Novels, on_delete=models.CASCADE);  # 章节所属信息
    img_freqency = models.ImageField(upload_to='img')
    img_wordcloud = models.ImageField(upload_to='img')
    img_renwu = models.ImageField(upload_to='img')



