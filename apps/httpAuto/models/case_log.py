from django.db import models
__all__ = ['CaseLog']


class CaseLog(models.Model):
    level_choice = (
        ('info', 'INFO'),
        ('debug', 'DEBUG'),
        ('error', 'ERROR'),
    )
    level = models.CharField(max_length=12, null=False, blank=False, default='INFO', choices=level_choice,
                             verbose_name='日志等级')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='执行时间')
    msg = models.TextField(null=True, blank=True, verbose_name='日志信息')
    result_id = models.CharField(max_length=64, null=False, blank=False, verbose_name="报告id")

    class Meta:
        verbose_name = '测试日志'
        verbose_name_plural = verbose_name
        db_table = 'case_log'
        ordering = ('create_time',)

    def __str__(self):
        return self.msg