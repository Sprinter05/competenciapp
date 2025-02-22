from core.models import *
from django.contrib.auth import get_user_model
import ollama

def insert_langs():
    file = open("resources/langs.csv", "r")

    for line in file:
        fields = line.split(",")
        response = ollama.embed(model="nomic-embed-text", input=fields[1])
        embedding = Embedding(embedding=response["embeddings"][0], text=fields[1])
        embedding.save()
        lang = Language(name=fields[1], description=fields[2], embedding_id=embedding)
        lang.save()

    file.close()

def insert_libs():
    file = open("resources/libs.csv", "r")

    for line in file:
        fields = line.split(",")
        response = ollama.embed(model="nomic-embed-text", input=fields[2])
        embedding = Embedding(embedding=response["embeddings"][0], text=fields[2])
        embedding.save()
        lib = Library(name=fields[2], description=fields[3], lang_id=fields[1] ,embedding_id=embedding)
        lib.save()

    file.close()

def insert_users():
    file = open("resources/users", "r")

    for line in file:
        fields = line.split(",")
        user = get_user_model
        user.objects.createuser(id=fields[0], name=fields[1], email="", password="")

    file.close()

def insert_user_lib():
    file = open("resources/userlib.csv", "r")

    for line in file:
        fields = line.split(";")
        lib_ids = fields[1].split(",")
        for id in lib_ids:
            userlib = UserLib(u_id=fields[0], lib_id=int(id))
            userlib.save()


def insert_user_lang():
    file = open("resources/userlang.csv", "r")

    for line in file:
        fields = line.split(";")
        lang_ids = fields[1].split(",")
        for id in lang_ids:
            userlib = UserLang(u_id=fields[0], lang_id=int(id))
            userlib.save()

insert_langs()
insert_libs()
insert_users()
insert_user_lib()
insert_user_lang()
