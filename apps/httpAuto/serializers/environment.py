from rest_framework import serializers

from apps.httpAuto.models.environment import Environment
from apps.httpAuto.serializers.base import BaseListSerializer, BaseSerializer


class EnvironmentNameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ('id', 'name', 'base_url')


class EnvironmentListSerializer(BaseListSerializer):
    class Meta:
        model = Environment
        fields = '__all__'


class EnvironmentSerializer(BaseSerializer):
    class Meta:
        model = Environment
        fields = '__all__'
