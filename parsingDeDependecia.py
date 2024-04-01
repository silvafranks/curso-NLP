import spacy

pln = spacy.load('pt_core_news_sm')

documento = pln('reserve uma passagem saindo de Guarulhos e chegando em Curitiba')


origem = documento[5]
destino = documento[9]

# print(list(destino.ancestors))

print(documento[0].is_ancestor(documento[2]))