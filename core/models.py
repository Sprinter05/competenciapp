from django.conf import settings
from django.db import models
from pgvector.django import VectorField
from django.contrib.auth.models import AbstractUser

# Holds the vector of each token
class Embedding(models.Model):
    id = models.AutoField(primary_key=True)
    embedding = VectorField(
        dimensions=1024,
        null=False,
        blank=False,
    )
    text=models.TextField(null = True) # text is the query given to ollama

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    embed_id = models.ForeignKey("core.Embedding", on_delete=models.CASCADE)

class Library(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    lang_id = models.ForeignKey("core.Language", on_delete=models.CASCADE)
    embed_id = models.ForeignKey("core.Embedding", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Libraries"

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    libs = models.ManyToManyField("core.Library", related_name="users")
    langs = models.ManyToManyField("core.Language", related_name="users")
