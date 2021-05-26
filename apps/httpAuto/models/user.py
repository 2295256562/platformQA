from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.httpAuto.models.base import BaseModel

__all__ = ['User']


class User(AbstractUser,BaseModel):
    gender_choice = (
        ('male', '男'),
        ('female', '女')
    )
    gender = models.CharField(null=False, blank=False, choices=gender_choice, default='male', max_length=6,
                              verbose_name='性别')
    roles_choice = (
        (0, '开发'),
        (1, '测试')
    )
    roles = models.IntegerField(null=False, blank=False, choices=roles_choice, default=1, verbose_name='角色')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        db_table = 'basic_user'
        ordering = ('username',)

    def __str__(self):
        return self.username
