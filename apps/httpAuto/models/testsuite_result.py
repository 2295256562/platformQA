import uuid
from django.db import models

__all__ = ['TestsuiteResult']

from apps.httpAuto.models.user import User


class TestsuiteResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    execute_time = models.DateTimeField(verbose_name='执行时间')
    elapsed_ms = models.DecimalField(max_digits=10, decimal_places=3, null=False, blank=False, verbose_name='执行耗时(ms)')
    passed_num = models.IntegerField(null=False, blank=False, verbose_name='通过数量')
    failed_num = models.IntegerField(null=False, blank=False, verbose_name='失败数量')
    total_num = models.IntegerField(null=False, blank=False, verbose_name='用例总数量')
    status_choice = (
        ('PASS', '通过'),
        ('PARTIAL_PASS', '部份通过'),
        ('FAIL', '失败')
    )
    status = models.CharField(max_length=12, null=False, blank=False, default='FAIL', choices=status_choice,
                              verbose_name='是否测试通过')
    product = models.ForeignKey(to='Product', related_name='+', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='所属项目')
    project_name = models.CharField(null=False, blank=False, max_length=128, verbose_name='项目名称')
    testsuite = models.ForeignKey(to='Testsuite', related_name='testsuite_result', on_delete=models.SET_NULL, null=True,
                                  blank=True, verbose_name='所属场景')
    testsuite_name = models.CharField(null=False, blank=False, max_length=128, verbose_name='场景名称')
    executor = models.ForeignKey(to=User, related_name='+', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='执行人')

    is_periodictask = models.BooleanField(null=False, blank=False, default=True, verbose_name='是否是定时任务')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_deleted = models.BooleanField(null=False, blank=False, default=False, verbose_name='是否已删除')

    class Meta:
        verbose_name = '场景结果'
        verbose_name_plural = verbose_name
        db_table = 'testsuite_result'
        ordering = ('-execute_time',)

    def __str__(self):
        return self.testsuite.name