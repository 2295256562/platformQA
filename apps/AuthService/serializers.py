from rest_framework import serializers
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from apps.AuthService.models import User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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
        user = User.objects.filter(username=username, is_active=True).first()
        if user is None:
            raise serializers.ValidationError({'data': '用户不存在'})
        if user and user.check_password(password):
            return user
        raise serializers.ValidationError({'data': '数据有误'})


class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data=validated_data)
        print(user)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password', "roles",)
