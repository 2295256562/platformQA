from rest_framework.mixins import CreateModelMixin


class CustomCreateModelMixin(CreateModelMixin):
    """
    Create a model instance.
    """
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.creator = self.request.user
        instance.save()
