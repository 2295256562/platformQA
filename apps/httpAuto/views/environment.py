from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from apps.httpAuto.filters.environment import EnvironmentNameFilter, EnvironmentFilter
from apps.httpAuto.models.environment import Environment
from apps.httpAuto.models.product import Product
from apps.httpAuto.serializers.environment import EnvironmentNameListSerializer, EnvironmentListSerializer, \
    EnvironmentSerializer
from platformQA.mixins import CustomCreateModelMixin


class EnvironmentNameListViewSet(ReadOnlyModelViewSet):
    """
    环境名称列表
    """
    queryset = Environment.objects.filter(is_deleted=False).values('id', 'name', 'base_url')
    serializer_class = EnvironmentNameListSerializer
    filter_class = EnvironmentNameFilter
    pagination_class = None


class EnvironmentListViewSet(ReadOnlyModelViewSet):
    """
    环境列表
    """
    queryset = Environment.objects.filter(is_deleted=False)
    serializer_class = EnvironmentListSerializer
    filter_class = EnvironmentFilter


class EnvironmentViewSet(CustomCreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    环境创建、更新
    """
    queryset = Environment.objects.filter(is_deleted=False)
    serializer_class = EnvironmentSerializer

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        projects = Product.objects.filter(default_environment_id=id, is_deleted=False)
        if projects:
            # 当存在项目使用此环境作为默认环境时，不允许删除该环境
            return Response(status=status.HTTP_200_OK, data='删除失败：该环境已被项目设定为默认环境，不允许被删除',
                            content_type='application/json')
        environment = Environment.objects.filter(id=id, is_deleted=False).first()
        if environment:
            environment.project.clear()
        Environment.objects.filter(id=id).update(is_deleted=True)
        return Response(status=status.HTTP_204_NO_CONTENT)