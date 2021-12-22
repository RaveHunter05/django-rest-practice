from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, BrandViewSet, ProductViewSet

router = routers.SimpleRouter()

router.register("category", CategoryViewSet)

router.register("brand", BrandViewSet)

router.register("product", ProductViewSet)

urlpatterns = router.urls
