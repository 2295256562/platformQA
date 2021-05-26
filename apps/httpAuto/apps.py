from django.apps import AppConfig


class HttpAutoConfig(AppConfig):
    name = 'apps.httpAuto'
    verbose_name = "接口自动化测试服务"

    def ready(self):
        pass
