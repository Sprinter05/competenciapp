from django.db import models
from pgvector.django import VectorField

# Create your models here.File "/home/markel/competenciapp/evnv/lib/python3.13/site-packages/django/db/backend
class Embedding(models.Model):
    id = models.AutoField(primary_key=True)
    embedding = VectorField(
        dimensions=768,
        null=False,
        blank=False,
    )
    text=models.TextField(null = True) # text is the query given to ollama

class Competence(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null = True)
    description = models.TextField(null = True)
    embedding_id = models.ForeignKey("core.Embedding", on_delete=models.CASCADE)

class UserAuth(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(null = True)

class UserCompetence(models.Model):
    uid = models.ForeignKey("core.UserAuth", primary_key=True, on_delete=models.CASCADE)
    cid = models.ForeignKey("core.Embedding", on_delete=models.CASCADE)
    unique_together = (("key1", "key2"))