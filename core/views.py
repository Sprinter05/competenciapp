from django.http import HttpResponse
from django.shortcuts import render
from pgvector.django import L2Distance
from models import Embeddings
from django.http import HttpResponse
from ollama import Client

client = Client(
    host="http://localhost:11434",
)

# Create your views here.
def index(request):
    return render(request, "index.html")

def profile(request):
    return HttpResponse("Profile page")

def search(request):
    return HttpResponse("Search page. Query: " + request.GET.get("q", ""))

def data(request):
    objs = Embeddings.objects.order_by(
        L2Distance('embedding', request.GET.get("q", "")))[:10]
    return HttpResponse(objs.values_list("text"))

def llama(request):
    prompt = request.GET.get("prompt", "")
    data = request.GET.get("data", "")
    response = client.generate(
        model='llama3.2', 
        prompt=f"Given this {data}, return the most relevant profiles according to {prompt}."
    )
    return HttpResponse(response)