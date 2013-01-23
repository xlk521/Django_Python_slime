#coding=utf8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.contrib import admin

class BaseModelManager(BaseUserManager , models.Manager):
    #django.contrib.auth.models.BaseUserManager
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None
        
class UpdateManager(BaseModelManager):
    pass

class Update(models.Model):
    class Meta:
        verbose_name_plural = u'更新历史'
        
    date= models.DateTimeField('更新日期',auto_now_add=True)
    content = models.TextField('更新内容')
    
    objects = UpdateManager()
    
    def __unicode__(self):
        return self.content


class UpdateAdmin(admin.ModelAdmin):
    list_display = ('date','content')
    

admin.site.register(Update, UpdateAdmin)