# utils.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView, ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from datetime import datetime


class MyJSONWebTokenAPIView(JSONWebTokenAPIView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            return response
        error_data = jwt_response_payload_error_handler(serializer, request)
        return Response(error_data, status=status.HTTP_200_OK)


def jwt_response_payload_handler(token, user=None, request=None):
    # 自定义返回 JWT
    return {
        "msg": "success",
        "status": 200,
        "data": [{
            # data自定义你接口想返回的信息
            'token': token,
            'username': user.username
        }]
    }


def jwt_response_payload_error_handler(serializer, request=None):
    return {
        "msg": "用户名或者密码错误",
        "status": 400,
        "detail": serializer.errors
    }


class MyObtainJSONWebToken(ObtainJSONWebToken, MyJSONWebTokenAPIView):
    pass


class MyRefreshJSONWebToken(RefreshJSONWebToken, MyJSONWebTokenAPIView):
    pass


class MyVerifyJSONWebToken(VerifyJSONWebToken, MyJSONWebTokenAPIView):
    pass


obtain_jwt_token = MyObtainJSONWebToken.as_view()
refresh_jwt_token = MyRefreshJSONWebToken.as_view()
verify_jwt_token = MyVerifyJSONWebToken.as_view()

