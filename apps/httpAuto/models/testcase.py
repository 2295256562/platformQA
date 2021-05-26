from django.db import models

from apps.httpAuto.models.base import BaseModel

__all__ = ['Testcase']


class Testcase(BaseModel):
    name = models.CharField(null=False, blank=False, max_length=128, unique=True, verbose_name='用例名称')
    url = models.TextField(null=False, blank=False, verbose_name='接口请求URL')
    headers = models.TextField(null=True, blank=True, verbose_name='接口请求头')
    request_data_type_choice = (
        ('Json', 'Json'),
        ('Form Data', 'Form Data'),
        ('x-www-form-urlencoded', 'urlencoded')
    )
    request_data_type = models.CharField(max_length=11, null=False, blank=False, default='Json',
                                         choices=request_data_type_choice, verbose_name='接口请求参数类型')
    request_params = models.TextField(null=True, blank=True, verbose_name='接口查询参数')
    asserts = models.TextField(null=True, blank=True, verbose_name='接口断言')
    extract = models.TextField(null=True, blank=True, verbose_name='接口提取')
    before = models.TextField(null=True, blank=True, verbose_name='接口前置')
    after = models.TextField(null=True, blank=True, verbose_name='接口后置')
    request_data = models.TextField(null=True, blank=True, verbose_name='接口请求参数')
    expect_result = models.TextField(null=True, blank=True, verbose_name='期望结果')
    level_choice = (
        ('LOW', '低'),
        ('NORMAL', '中'),
        ('HIGH', '高'),
        ('HIGHER', '更高'),
    )
    level = models.CharField(max_length=12, null=False, blank=False, default='NORMAL', choices=level_choice,
                             verbose_name='用例级别')
    api = models.ForeignKey(to='Api', related_name='testcase', on_delete=models.SET_NULL, null=True, blank=True,
                            verbose_name='所属接口')

    class Meta:
        verbose_name = '测试用例'
        verbose_name_plural = verbose_name
        db_table = 'testcase'
        ordering = ('-update_time',)

    def __str__(self):
        return self.name
