from django.db import models


class Types(models.Model):
    name = models.CharField(max_length=20, verbose_name="小说名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "小说分类信息"
        verbose_name_plural = "小说分类信息"
# Create your models here.
class Novels(models.Model):
    novel_type=models.ForeignKey('Types',on_delete=False,null = True, blank=True)
    novel_Id=models.IntegerField(primary_key=True,);#字段ID
    novel_name=models.CharField(max_length=20); #字段名
    novel_author=models.CharField(max_length=20);#作者名
    novel_pv=models.IntegerField(default=0);#点击量
    novel_img=models.CharField(max_length=100);#封面路径
    # novel_type=models.CharField(max_length=20);#小说类型
    novel_des=models.CharField(max_length=900);#小说介绍
    novel_freqency=models.ImageField( upload_to='img',null = True, blank=True)
    novel_wordcloud = models.ImageField(upload_to='img', null=True, blank=True)
    novel_people= models.ImageField(upload_to='img', null=True, blank=True)
    novel_addTime=models.DateTimeField("Date published",auto_now=True);#发表日期
    def __str__ (self):
        return self.novel_name;
    def toDict(self):
        return {
                # 'novel_type':self.novel_type.id,
                'novel_Id':self.novel_Id,
                'novel_img':self.novel_img,
                'novel_name':self. novel_name

        }
class Chart(models.Model):
    novel=models.ForeignKey(Novels,on_delete=models.CASCADE);#章节所属信息
    novel_idx=models.IntegerField();#章节号
    novel_title=models.CharField(max_length=100);#章节标题
    novel_cont=models.TextField(max_length=5000);#章节内容
    
    class Meta:
        unique_together=(("novel","novel_idx"),)
    def __str__(self):
        return self.novel_title;

