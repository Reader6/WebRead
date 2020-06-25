from django.db import models


class User(models.Model):
    '''用户表'''

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    head_img=models.ImageField(upload_to="img",verbose_name="头像",null=True,blank=True)

    def toDict(self):
        return {'id':self.id,'username':self.name,'password':self.password,'email':self.email,'c_time':self.c_time,'head_img':self.head_img}
    def __str__(self):
        return self.name

    class Meta:
        db_table='user'
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
# Create your models here.

