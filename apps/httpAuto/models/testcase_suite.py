from django.db import models

from apps.httpAuto.models.base import BaseModel

__all__ = ['Testsuite']


class Testsuite(BaseModel):
    level_choice = (
        ('LOW', '低'),
        ('NORMAL', '中'),
        ('HIGH', '高'),
        ('HIGHER', '更高'),
    )
    level = models.CharField(max_length=12, null=False, blank=False, default='NORMAL', choices=level_choice,
                             verbose_name='场景级别')
    global_variables = models.TextField(null=True, blank=True, verbose_name='场景全局参数')
    product = models.ForeignKey(to='Product', related_name='testsuite', on_delete=models.SET_NULL, null=True,
                                blank=True, verbose_name='所属项目')
    testcases = models.ManyToManyField(to='Testcase', related_name='testsuite',
                                       # through_fields=('testsuite', 'testcase'), through='Testsuite2Testcase',
                                       verbose_name='测试用例')

    class Meta:
        verbose_name = '测试场景'
        verbose_name_plural = verbose_name
        db_table = 'testsuite'
        ordering = ('-update_time',)

    def __str__(self):
        return self.name
