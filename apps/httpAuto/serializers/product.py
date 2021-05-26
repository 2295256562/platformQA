
from rest_framework import serializers

from apps.httpAuto.models.product import Product
from apps.httpAuto.serializers.base import BaseListSerializer, TidyUserSerializer, BaseSerializer


class ProductNameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name',)


class ProjectListSerializer(BaseListSerializer):
    members = TidyUserSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProjectSerializer(BaseSerializer):
    def create(self, validated_data):
        members = validated_data.pop('members')
        validated_data['creator'] = self.context['request'].user
        validated_data['modifier'] = self.context['request'].user
        project = Product.objects.create(**validated_data)
        project.members.set(members)
        return project

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'members': {'required': False}
        }