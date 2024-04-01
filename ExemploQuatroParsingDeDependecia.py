import spacy
from spacy import displacy

pln = spacy.load('pt_core_news_sm')

documento = pln('Que locais podemos visitar em curitiba e para ficar em guarulhos')
# tarefas = documento[3].pos_, documento[10].pos_
# locais = documento[6].pos_, documento[13].pos_

# fazer o for procurando o "_pos" de mesa e de restaurante
lugares = documento[5], documento[10]
acoes = documento[3], documento[8]

# for local in lugares:
#     for acao in local.ancestors:
#         if acao in acoes:
#             print("{} para {}".format(local, acao))
#             break

displacy.serve(documento, style='dep',options={displacy:90})