from django.shortcuts import render
from pgvector.django import L2Distance
from models import Embeddings
from django.http import HttpResponse

# Create your views here.
def data(vector):
    objs = Embeddings.objects.order_by(
        L2Distance('embedding', vector))[:10]
    return HttpResponse(objs)