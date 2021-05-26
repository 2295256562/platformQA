
import django_filters


__all__ = ['EnvironmentNameFilter', 'EnvironmentFilter']

from apps.httpAuto.models.environment import Environment


class EnvironmentNameFilter(django_filters.rest_framework.FilterSet):
    """
    环境名称过滤
    """
    project = django_filters.CharFilter(method='project_filter')

    def project_filter(self, queryset, name, value):
        return queryset.filter(project__id=value)

    class Meta:
        model = Environment
        fields = ['project']


class EnvironmentFilter(django_filters.rest_framework.FilterSet):
    """
    环境过滤
    """
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    is_active = django_filters.BooleanFilter(field_name='is_active', lookup_expr='exact')

    class Meta:
        model = Environment
        fields = ['name', 'is_active']
