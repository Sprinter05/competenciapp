from django.db import models
from pgvector.django import VectorField

# Create your models here.
class Embeddings(models.Model):
    id = models.AutoField(primary_key=True)
    embedding = VectorField(
        dimensions=4096,
        null=False,
        blank=False,
    )
    text=models.TextField

class Competences(models.Model):
    id = models.ForeignKey(Embeddings.id, primary_key=True)
    name = models.TextField
    description = models.TextField
    embedding_id = models.AutoField

class UserAuth(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField

class UserCompetences(models.Model):
    uid = models.ForeignKey(UserAuth.id, primary_key=True)
    cid = models.ForeignKey(Competences.id, primary_key=True)