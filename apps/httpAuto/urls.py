from rest_framework.routers import DefaultRouter

from apps.httpAuto.views.userView import LoginViewSet

routers = DefaultRouter()

routers.register(r'^login', LoginViewSet, basename="login")

urlpatterns = routers.urls
