from spacy.lang.pt.stop_words import STOP_WORDS
import spacy

pln = spacy.load('pt_core_news_sm')

documento = pln('Estou aprendendo processamento de linguagem natural, curso em São Paulo')

# STOP_WORDS

for token in documento: 
    # if not pln.vocab[token.text].is_stop:
        print(token.text, token.pos_)