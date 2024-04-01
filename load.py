import spacy

pln = spacy.load('pt_core_news_sm')

documento = pln('Estou aprendendo processamento de linguagem natural, curso em São Paulo')

# for token in documento:
#     print(token.text, token.pos_)

# for token in documento:
#     if(token.pos_ == 'PROPN' ):
#         print(token.text)

for token in documento:
    print(token.text, token.lemma_)

