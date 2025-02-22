from core.models import *
from django.contrib.auth.models import User
import ollama

def insert_langs():
    file = open("resources/langs.csv", "r")

    for line in file:
        fields = line.split(",")
        response = ollama.embed(model="mxbai-embed-large", input=fields[1])
        embedding = Embedding(embedding=response["embeddings"][0], text=fields[1])
        embedding.save()
        lang = Language(name=fields[1], description=fields[2], embed_id=embedding)
        lang.save()

    file.close()

def insert_libs():
    file = open("resources/libs.csv", "r")

    for line in file:
        fields = line.split(",")
        response = ollama.embed(model="mxbai-embed-large", input=fields[2])
        embedding = Embedding(embedding=response["embeddings"][0], text=fields[2])
        embedding.save()
        lib = Library(name=fields[2], description=fields[3], lang_id=Language(id=int(fields[1])) ,embed_id=embedding)
        lib.save()

    file.close()

def insert_users():
    file = open("resources/users.csv", "r")

    for line in file:
        fields = line.split(",")
        user = User.objects.create_user(username=fields[1], email="", password="")
        user.save()
        
    file.close()

def insert_user_lib():
    file = open("resources/userlib.csv", "r")

    for line in file:
        fields = line.split(";")
        lib_ids = fields[1].split(",")
        for id in lib_ids:
            userlib = UserLib(u_id=User(id=int(fields[0])), lib_id=Library(id=int(id)))
            userlib.save()


def insert_user_lang():
    file = open("resources/userlang.csv", "r")

    for line in file:
        fields = line.split(";")
        lang_ids = fields[1].split(",")
        for id in lang_ids:
            userlang = UserLang(u_id=User(id=int(fields[0])), lang_id=Language(id=int(id)))
            userlang.save()

insert_langs()
insert_libs()
insert_users()
insert_user_lib()
insert_user_lang()
