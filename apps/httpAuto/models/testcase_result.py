import uuid

from django.db import models

from apps.httpAuto.models.user import User


class Testcase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.TextField(null=False, blank=False, verbose_name='接口请求URL')
    method_choice = (
        ('GET', 'GET'),
        ('PUT', 'PUT'),
        ('POST', 'POST'),
        ('PATCH', 'PATCH'),
        ('DELETE', 'DELETE')
    )
    method = models.CharField(max_length=11, null=False, blank=False, default='GET', choices=method_choice,
                              verbose_name='接口请求方法')
    headers = models.TextField(null=True, blank=True, verbose_name='接口请求头信息')
    request_data_type_choice = (
        ('Params', 'Params'),
        ('Json', 'Json'),
        ('Form Data', 'Form Data'),
        ('x-www-form-urlencoded', 'urlencoded')
    )
    request_data_type = models.CharField(max_length=11, null=False, blank=False, default='Json',
                                         choices=request_data_type_choice, verbose_name='接口请求参数类型')
    request_data = models.TextField(null=True, blank=True, verbose_name='接口请求参数')
    actual_status_code = models.CharField(max_length=11, null=False, blank=False, verbose_name='实际响应状态码')
    actual_response_data = models.TextField(null=False, blank=False, verbose_name='实际响应结果')
    execute_time = models.DateTimeField(verbose_name='执行时间')
    elapsed_ms = models.DecimalField(max_digits=10, decimal_places=3, null=False, blank=False, verbose_name='响应时长(ms)')
    status_choice = (
        ('PASS', '通过'),
        ('FAIL', '失败')
    )
    status = models.CharField(max_length=11, null=False, blank=False, default='FAIL', choices=status_choice,
                              verbose_name='是否测试通过')
    failure_reason = models.TextField(null=True, blank=True, verbose_name='测试未通过原因')
    product = models.ForeignKey(to='Product', related_name='+', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='所属项目')
    project_name = models.CharField(null=False, blank=False, max_length=128, verbose_name='项目名称')
    api = models.ForeignKey(to='Api', related_name='+', on_delete=models.SET_NULL, null=True, blank=True,
                            verbose_name='所属接口')
    api_name = models.CharField(null=False, blank=False, max_length=128, verbose_name='接口名称')
    testcase = models.ForeignKey(to='Testcase', related_name='testcase_result', on_delete=models.SET_NULL, null=True,
                                 blank=True, verbose_name='所属用例')
    testcase_name = models.CharField(null=False, blank=False, max_length=128, verbose_name='用例名称')
    testsuite_result = models.ForeignKey(to='TestsuiteResult', related_name='testcase_result',
                                         on_delete=models.CASCADE, null=True, blank=True, verbose_name='所属场景结果')
    testsuite_name = models.CharField(null=True, blank=True, max_length=128, verbose_name='场景名称')
    executor = models.ForeignKey(to=User, related_name='+', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='执行人')
    is_periodictask = models.BooleanField(null=False, blank=False, default=True, verbose_name='是否是定时任务')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_deleted = models.BooleanField(null=False, blank=False, default=False, verbose_name='是否已删除')

    class Meta:
        verbose_name = '测试用例'
        verbose_name_plural = verbose_name
        db_table = 'testcase'
        ordering = ('-update_time',)

    def __str__(self):
        return self.name
