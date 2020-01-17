from django.db import transaction
from rest_framework import serializers
from app import models


class AppSerializer(serializers.ModelSerializer):

    api_key = serializers.CharField(read_only=True, )

    class Meta:
        model = models.App
        fields = ("id", "name", "api_key")

    @transaction.atomic()
    def save(self, **kwargs):
        super().save(**kwargs)
        self.instance.set_api_key()
