from rest_framework import serializers

from apps.AuthService.models import User

__all__ = ['BaseSerializer', 'BaseListSerializer', 'TidyUserSerializer']


class TidyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_deleted')


class BaseSerializer(serializers.ModelSerializer):
    modifier = serializers.HiddenField(default=serializers.CurrentUserDefault())


class BaseListSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    modifier = TidyUserSerializer()
