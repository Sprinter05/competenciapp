import ollama
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from pgvector.django import CosineDistance

from .models import Embedding, Library, Language


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
        results = langs
    elif category == 2:  # Libraries
        libs = Library.objects.all().filter(
            embed_id__in=objs.values_list("id")
        )
        results = libs
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

def prompt(request):
    query = request.GET.get("q", "")
    # ? Max amount of keywords
    base = "Only output in your following prompt a comma separated list of programming languages with programming libraries and/or frameworks keywords for the following text, up to a max of 5 keywords: "

    keywords = ollama.chat(
        model='llama3.2:1b',
        messages=[{
            "role": "user",
            "content": f"{base} {query}" 
        }]
    )

    matrixes = []
    words = keywords.split(",")
    for word in words:
        embed = ollama.embeddings(
            prompt = word,
            model = "mxbai-embed-large"
        )
        matrixes.append(embed)

    embeds = []
    for matrix in matrixes:
        embeds.append(Embedding.objects.annotate(
            distance = CosineDistance(
                'embedding', 
                matrix["embedding"]
            )
        ).filter(distance__lte = 0.5).order_by("distance"))

    # TODO: Get all user objects