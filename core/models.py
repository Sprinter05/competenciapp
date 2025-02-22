from django.db import models
from pgvector.django import VectorField

# Holds the vector of each token
class Embedding(models.Model):
    id = models.AutoField(primary_key=True)
    embedding = VectorField(
        dimensions=768,
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

class UserAuth(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(null=True)

# Associates a library to the user competent at said library
# This table can also be used to associate languages to users
class UserLib(models.Model):
    id = models.AutoField(primary_key=True)
    u_id = models.ForeignKey("core.UserAuth", on_delete=models.CASCADE)
    lib_id = models.ForeignKey("core.Library", on_delete=models.CASCADE)