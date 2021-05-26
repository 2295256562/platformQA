from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from apps.httpAuto import LoginSerializer
from utils.response import success_response


class LoginViewSet(ViewSet):
    authentication_classes = []
    permission_classes = []

    def login(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})  # 自定义序列化
        serializer.is_valid(raise_exception=True)  # 序列化校验
        token = serializer.context.get('token')  # 获取token
        return JsonResponse(success_response({"token": token}))
