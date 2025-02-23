import ollama
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pgvector.django import CosineDistance

from .models import Embedding, Library, Language, AuthUser


# Create your views here.
def index(request):
    return render(request, "index.html")


def search(request):
    query = request.GET.get("q", "")
    dist = request.GET.get("s", 0.5)
    category = request.GET.get("category", 0)

    try:
        dist = float(dist)
        category = int(category)
    except ValueError as e:
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

    data = {}

    if category == 0:  # All (TODO: Fix this)
        pass
    elif category == 1:  # Languages
        langs = Language.objects.all().filter(
            embed_id__in=objs.values_list("id")
        )
        for technology in langs:
            data[technology] = AuthUser.objects.filter(langs=technology)
    elif category == 2:  # Libraries
        libs = Library.objects.all().filter(
            embed_id__in=objs.values_list("id")
        )
        for technology in libs:
            data[technology] = AuthUser.objects.filter(libs=technology)
    else:
        return redirect("index")


    print(data)
    return render(request, "result.html",
                  context={"search": query, "distance": dist, "category": category, "data": data})


@login_required
def profile(request):
    user = AuthUser.objects.get(pk=request.user.id)
    context = {
        'user': user,
        'languages': user.langs.all(),
        'libraries': user.libs.all(),
        'all_languages': Language.objects.all()
    }
    return render(request, "profile.html", context)


def get_user_profile(request, uid):
    user = AuthUser.objects.get(pk=uid)
    context = {
        'user': user,
        'languages': user.langs.all(),
        'libraries': user.libs.all(),
        'all_languages': Language.objects.all()
    }
    print()
    return render(request, "profile.html", context)

@login_required
def add_language(request):
    return HttpResponse("Add Language")


@login_required
def add_library(request):
    return HttpResponse("Add Library")

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