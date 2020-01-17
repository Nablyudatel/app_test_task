from rest_framework import routers
from app import api_views

router = routers.DefaultRouter()
router.register(r"apps", api_views.AppViewSet)
