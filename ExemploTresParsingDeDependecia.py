import spacy
from spacy import displacy

pln = spacy.load('pt_core_news_sm')

documento = pln('Será que vai fazer calor? ou Será que frio fará ?')
# tarefas = documento[3].pos_, documento[10].pos_
# locais = documento[6].pos_, documento[13].pos_

# fazer o for procurando o "_pos" de mesa e de restaurante
# tarefas = documento[3], documento[10]
# locais = documento[6], documento[13]
# print(list(documento[9].children))

verbs =  []
filhosVerb = []

teste = documento[3] #VERB fazer

for token in documento:
    if token.pos_ == "VERB":
        verbo = token
        listaAuxiliar = list(verbo.children)
        for filho in listaAuxiliar:
            if filho.pos_ == "NOUN":
                substantivo = filho
                print("{} --> {}".format(verbo, substantivo))
                break

displacy.serve(documento, style='dep',options={displacy:90})