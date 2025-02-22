import ollama
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pgvector.django import CosineDistance

from .models import Embedding, Library, Language, UserLib, UserLang


# Create your views here.
def index(request):
    return render(request, "index.html")

def profile(request):
    return HttpResponse("Profile page")

def search(request):
    query = request.GET.get("q", "")
    dist = request.GET.get("s", 0.5)
    category = request.GET.get("category", 0)

    try:
        dist = float(dist)
        category = int(category)
    except ValueError as e:
        print(e)
        return redirect("index")

    neighbours = ollama.embeddings(
        prompt = query,
        model = "mxbai-embed-large"
    )

    # Get all matching embeds
    objs = Embedding.objects.annotate(
        distance = CosineDistance(
            'embedding', 
            neighbours["embedding"]
        )
    ).filter(distance__lte = dist).order_by("distance")

    results = []
    if category == 0:  # All (TODO: Fix this)
        results = None
    elif category == 1:  # Languages
        langs = Language.objects.all().filter(
            embed_id__in=objs.values_list("id")
        )
        results = UserLang.objects.all().filter(
            lang_id__in=langs.values_list("id")
        )
    elif category == 2:  # Libraries
        libs = Library.objects.all().filter(
            embed_id__in=objs.values_list("id")
        )
        results = UserLib.objects.all().filter(
            lib_id__in=libs.values_list("id")
        )
    else:
        return redirect("index")

    print(dist)
    print(type(dist))

    return render(request, "result.html",
                  context={"search": query, "distance": dist, "results": results, "category": category})


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
