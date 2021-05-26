import uuid
from django.db import models

__all__ = ['BaseModel']


class BaseModel(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    remark = models.TextField(null=True, blank=True, verbose_name='备注')
    is_deleted = models.BooleanField(null=False, blank=False, default=False, verbose_name='是否已删除')
    create_user = models.CharField(max_length=36, verbose_name='创建人')

    class Meta:
        abstract = True
