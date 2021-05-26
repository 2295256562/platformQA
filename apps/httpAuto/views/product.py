from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from apps.httpAuto.filters.product import ProjectFilter
from apps.httpAuto.models.interface import Api
from apps.httpAuto.models.product import Product
from apps.httpAuto.serializers.product import ProductNameListSerializer, ProjectListSerializer, ProjectSerializer
from platformQA.mixins import CustomCreateModelMixin

__all__ = ['ProjectNameListViewSet', 'ProjectListViewSet', 'ProjectViewSet']


class ProjectNameListViewSet(ReadOnlyModelViewSet):
    """
    项目名称列表
    """
    serializer_class = ProductNameListSerializer
    pagination_class = None

    def get_queryset(self):
        product = Product.objects.filter(is_deleted=False).values('id', 'name')
        return product


class ProjectListViewSet(ReadOnlyModelViewSet):
    """
    项目列表
    """
    serializer_class = ProjectListSerializer
    filter_class = ProjectFilter

    def get_queryset(self):
        projects = Product.objects.filter(is_deleted=False)
        return projects


class ProjectViewSet(CustomCreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    项目创建、更新
    """
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        user = self.request.user
        instance = serializer.save()
        instance.creator = user
        instance.save()

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        apis = Api.objects.filter(project_id=id, is_deleted=False)
        if apis:
            return Response(status=status.HTTP_200_OK, data='删除失败：该项目中存在接口，不允许被删除', content_type='application/json')

        project = Product.objects.filter(id=id, is_deleted=False).first()
        if project:
            project.members.clear()
            project.is_deleted = True
            project.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
