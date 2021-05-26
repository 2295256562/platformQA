import django_filters


__all__ = ['ProjectFilter']

from apps.httpAuto.models.product import Product


class ProjectFilter(django_filters.rest_framework.FilterSet):
    """
    项目过滤
    """
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name']