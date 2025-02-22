from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from pgvector.django import CosineDistance
from .models import Embedding
from django.http import HttpResponse
import ollama

# Create your views here.
def index(request):
    return render(request, "index.html")

def profile(request):
    return HttpResponse("Profile page")

def search(request):
    query = request.GET.get("q", "")
    dist = request.GET.get("s", 0.5)
    neighbours = ollama.embeddings(
        prompt = query,
        model = "nomic-embed-text"
    )
    objs = Embedding.objects.annotate(
        distance = CosineDistance(
            'embedding', 
            neighbours["embedding"]
        )
    ).filter(distance__lte = dist).order_by("distance")

    return render(request, "result.html", context={"technologies": objs, "search": query, "distance": dist})


@login_required
def profile(request):
    # Obtener los lenguajes del usuario
    """

    user_languages = UserLang.objects.filter(u_id__username=request.user.username)
    languages = [ul.lang_id for ul in user_languages]

    # Obtener las librerías del usuario
    user_libraries = UserLib.objects.filter(u_id__username=request.user.username)
    libraries = [ul.lib_id for ul in user_libraries]
    """

    context = {
        'languages': None,
        'libraries': None
    }

    return render(request, "profile.html", context)