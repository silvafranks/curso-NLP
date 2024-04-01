import spacy

pln = spacy.load('pt_core_news_sm')

documento = pln('Reserva de uma mesa para o restaurante e de um táxi para o hotel')
# tarefas = documento[3].pos_, documento[10].pos_
# locais = documento[6].pos_, documento[13].pos_

# fazer o for procurando o "_pos" de mesa e de restaurante
tarefas = documento[3], documento[10]
locais = documento[6], documento[13]

print(tarefas, locais)

for local in locais:
    print(local)
    print(type(local))
    for objeto in local.ancestors:
        if objeto in tarefas:
            print("Reserva de {} é para o {}".format(objeto, local))
            break



