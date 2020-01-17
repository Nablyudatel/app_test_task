import secrets

from django.db import models


class App(models.Model):

    name = models.CharField(max_length=20)
    api_key = models.CharField(max_length=100, unique=True)

    def set_api_key(self):
        if self.api_key:
            raise RuntimeError("Ключ приложения уже был создан")
        api_key = "api_key_" + secrets.token_urlsafe()
        self.api_key = api_key
        self.save()
