from django.http import HttpResponse
from django.shortcuts import render
from pgvector.django import L2Distance
from .models import Embedding
from django.http import HttpResponse
import ollama

# Create your views here.
def index(request):
    return render(request, "index.html")

def profile(request):
    return HttpResponse("Profile page")

def search(request):
    return HttpResponse("Search page. Query: " + request.GET.get("q", ""))

def data(request):
    query = request.GET.get("q", "")
    neighbours = ollama.embeddings(
        prompt = query,
        model = "nomic-embed-text"
    )
    objs = Embedding.objects.order_by(
        L2Distance('embedding', neighbours["embedding"]))[:10]
    return HttpResponse(objs)

def llama(request):
    prompt = request.GET.get("prompt", "")
    data = request.GET.get("data", "")
    
    response = ollama.generate(
        model='llama3.2', 
        prompt=f"Given this {data}, return the most relevant profiles according to {prompt}."
    )
    return HttpResponse(response)