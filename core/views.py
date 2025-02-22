from django.http import HttpResponse
from django.shortcuts import render
from pgvector.django import CosineDistance
from .models import Embedding, Library, Language, UserLib, UserLang
from django.http import HttpResponse
import ollama

# Create your views here.
def index(request):
    return render(request, "index.html")

def profile(request):
    return HttpResponse("Profile page")

def search(request):
    query = request.GET.get("q", "")
    dist = request.GET.get("s", "")

    # Get ollama vector
    neighbours = ollama.embeddings(
        prompt = query,
        model = "nomic-embed-text"
    )

    # Get all matching embeds
    objs = Embedding.objects.annotate(
        distance = CosineDistance(
            'embedding', 
            neighbours["embedding"]
        )
    ).filter(distance__lte = dist).order_by("distance")

    # Get all languages by id
    langs = Language.objects.all().filter(
        embed_id__in = objs.values_list("id")
    )

    # Get all libraries by id
    libs = Library.objects.all().filter(
        embed_id__in = objs.values_list("id")
    )

    # Get related users
    ulangs = UserLang.objects.all().filter(
        lang_id__in = libs.values_list("id")
    )
    ulibs = UserLib.objects.all().filter(
        lib_id__in = libs.values_list("id")
    )

    search = ulangs.values() + ulibs.values()
    return render(request, "result.html", context={"technologies": search})