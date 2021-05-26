from django.db import models

from apps.httpAuto.models.base import BaseModel
from apps.httpAuto.models.user import User


class Product(BaseModel):
    name = models.CharField(null=False, blank=False, max_length=64, unique=True, verbose_name='名称')
    global_variables = models.TextField(null=True, blank=True, verbose_name='项目全局参数')
    members = models.ManyToManyField(User, related_name='product', verbose_name='项目成员')

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name
        db_table = 'product'
        ordering = ('name',)

    def __str__(self):
        return self.namea
