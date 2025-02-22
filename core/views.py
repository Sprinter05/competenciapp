from django.contrib.auth.decorators import login_required
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
    dist = request.GET.get("s", 0.5)
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
        lang_id__in = langs.values_list("id")
    )
    ulibs = UserLib.objects.all().filter(
        lib_id__in = libs.values_list("id")
    )

    search = ulangs.values() + ulibs.values()
    return render(request, "result.html", context={"technologies": search})


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

def addlang(request):
    lang = Language(
        name = request.POST.get("l", "")
    )