from rest_framework import routers
from .api import EnglishWordViewSet

router = routers.DefaultRouter()
router.register('api/projects', EnglishWordViewSet, 'projects')

urlpatterns = router.urls