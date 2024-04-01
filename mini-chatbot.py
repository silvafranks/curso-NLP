import spacy
from spacy import displacy

pln = spacy.load('pt_core_news_sm')

documento = pln('Que locais podemos visitar em curitiba e para ficar em guarulhos')

tarefas = []
locaisSubstantivos = []

for tarefa in documento:
    if tarefa.pos_ == "VERB":
        tarefas.append(tarefa)

for local in documento:
    if local.pos_ == "PROPN" or local.pos_== "NOUN":
        locaisSubstantivos.append(local)


for local in locaisSubstantivos:
    for objeto in local.ancestors:
        if objeto in tarefas:
            print(" {} --> {}".format(objeto, local))
            break
# displacy.serve(documento, style='dep',options={displacy:90})