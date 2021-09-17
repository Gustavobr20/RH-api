from rest_framework.routers import DefaultRouter

from .views import FuncionariosViewSet

router = DefaultRouter()
router.register(r'', FuncionariosViewSet, basename='funcionarios')

funcionarios_urls = router.urls
