from rest_framework import serializers
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from apps.httpAuto.models import BaseUser


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ('username', 'password')

    def validate(self, attrs):
        user = self._get_user(attrs)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.context['token'] = token
        return attrs

    def _get_user(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = BaseUser.objects.filter(username=username, is_active=True).first()
        if user and user.check_password(password):
            return user
        raise serializers.ValidationError({'data': '数据有误'})
