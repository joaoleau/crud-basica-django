from django.db import models

class User(models.Model):
    nickname = models.CharField(primary_key=True, max_length=100, default='')
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    age = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Nome: {self.name} | Email: {self.email}"