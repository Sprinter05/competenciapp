from core.models import *
import ollama

file = open("resources/dataset-1.csv", "r")

for line in file:
    fields = line.split(",")
    response = ollama.embed(model="nomic-embed-text", input=fields[1])
    embedding = Embedding(embedding= response["embeddings"][0], text = fields[1])
    embedding.save()
    competence = Competence(name = fields[1], description = fields[1], embedding_id = embedding)
    competence.save()
    

file.close()