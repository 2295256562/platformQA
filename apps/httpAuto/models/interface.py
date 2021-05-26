from django.db import models
from apps.httpAuto.models.base import BaseModel
from apps.httpAuto.models.user import User


class Api(BaseModel):
    url = models.TextField(null=False, blank=False, verbose_name='接口请求URL')
    method_choice = (
        ('GET', 'GET'),
        ('PUT', 'PUT'),
        ('POST', 'POST'),
        ('PATCH', 'PATCH'),
        ('DELETE', 'DELETE'),
        ('OPTIONS', 'OPTIONS'),
        ('HEAD', 'HEAD'),
    )
    method = models.CharField(max_length=11, null=False, blank=False, default='GET', choices=method_choice,
                              verbose_name='接口请求方法')
    headers = models.TextField(null=True, blank=True, verbose_name='接口请求头信息')

    project = models.ForeignKey(to='Product', related_name='api', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='所属项目')
    version = models.ForeignKey(to='Version', related_name='api', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='所属版本')
    testers = models.ManyToManyField(User, related_name='api', verbose_name='测试人员')
    developers = models.ManyToManyField(User, related_name='api', verbose_name='开发人员')

    class Meta:
        verbose_name = '接口'
        verbose_name_plural = verbose_name
        db_table = 'interface'
        ordering = ('-update_time',)

    def __str__(self):
        return self.name
