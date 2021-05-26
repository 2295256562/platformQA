from django.db import models
from apps.httpAuto.models.base import BaseModel


class Version(BaseModel):
    name = models.CharField(null=False, blank=False, max_length=128, unique=True, verbose_name='名称')

    class Meta:
        verbose_name = '测试版本'
        verbose_name_plural = verbose_name
        db_table = 'version'
        ordering = ('name',)

    def __str__(self):
        return self.name
