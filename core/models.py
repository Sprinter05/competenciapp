from django.contrib.auth.models import AbstractUser
from django.db import models
from pgvector.django import VectorField


# Holds the vector of each token
class Embedding(models.Model):
    id = models.AutoField(primary_key=True)
    embedding = VectorField(
        dimensions=1024,
        null=False,
        blank=False,
    )
    text = models.TextField(null=True)  # text is the query given to ollama

    def __str__(self):
        return self.text


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    embed_id = models.ForeignKey("core.Embedding", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Library(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    lang_id = models.ForeignKey("core.Language", on_delete=models.CASCADE)
    embed_id = models.ForeignKey("core.Embedding", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Libraries"

    def __str__(self):
        return self.name


class AuthUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    libs = models.ManyToManyField("core.Library", related_name="users")
    langs = models.ManyToManyField("core.Language", related_name="users")

    def __str__(self):
        return self.username
