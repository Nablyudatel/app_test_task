from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from app.models import App
from app.serializers import AppSerializer
from rest_framework.decorators import action


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

    @action(detail=False, methods=["get"], url_path=r"test/(?P<api_key>[^/.]+)")
    def test(self, request, api_key, pk=None):
        app = get_object_or_404(App, api_key=api_key)
        s = AppSerializer(instance=app)
        return Response(s.data)
