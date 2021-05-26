from django.db import models


__all__ = ['Environment']

from apps.httpAuto.models.base import BaseModel


class Environment(BaseModel):
    name = models.CharField(null=False, blank=False, max_length=128, unique=True, verbose_name='名称')
    base_url = models.CharField(null=False, blank=False, max_length=256, verbose_name='环境地址')
    global_variables = models.TextField(null=True, blank=True, verbose_name='测试环境全局参数')
    global_headers = models.TextField(null=True, blank=True, verbose_name='测试环境全局headers')

    class Meta:
        verbose_name = '测试环境'
        verbose_name_plural = verbose_name
        db_table = 'environment'
        ordering = ('name',)

    def __str__(self):
        return self.name