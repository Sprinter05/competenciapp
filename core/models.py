from django.db import models
from django.conf import settings
from pgvector.django import VectorField

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

class UserLib(models.Model):
    u_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lib_id = models.ForeignKey("core.Library", on_delete=models.CASCADE)

class UserLang(models.Model):
    u_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lang_id = models.ForeignKey("core.Language", on_delete=models.CASCADE)