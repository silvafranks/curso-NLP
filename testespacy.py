import pandas as pd
import string
import spacy
import random
import seaborn as  sns
import numpy as np
from spacy.lang.pt.stop_words import STOP_WORDS

stop_words = STOP_WORDS
pontuacoes = string.punctuation
base_dados = pd.read_csv("/home/consultor/Documentos/curso-NLP/arquivos/base_treinamento.txt", encoding= 'utf-8')

# sns.countplot(base_dados["emocao"], label = 'Contagem')

teste = "Estou aprendendo processamento de 1 10 24 linguagem natural, Curso em Curitiba"
pln = spacy.load('pt_core_news_sm')


def preprocessamento(texto):
    texto = texto.lower()
    documento = pln(texto)

    lista = []
    for token in documento:
        lista.append(token.lemma_)

    lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in pontuacoes]
    lista = ' '.join([str(elemento) for elemento in lista if not  elemento.isdigit()])
    return lista


# print(base_dados.head(10))
# print(preprocessamento(teste))

base_dados['texto'] = base_dados['texto'].apply(preprocessamento)
# print( base_dados)

base_dados_final = []

for texto, emocao in zip(base_dados['texto'], base_dados['emocao']):
    # print(texto, emocao)
    if emocao == 'alegria':
        dic = ({'ALEGRIA': True, 'MEDO': False})
    elif emocao == 'emocao':
        dic = ({'ALEGRIA': False, 'MEDO': True})

    base_dados_final.append([texto, dic.copy()])


print(base_dados_final)