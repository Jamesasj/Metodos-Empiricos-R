#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:34:10 2018

@author: james
"""
import math
from collections import Counter
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

def vetorizar(texto):
    return texto.replace(',','').replace('.','').replace(':','').replace(';','').replace('!','').replace('?','').lower().split()

arquivo = "/home/james/Documentos/Metodos-Empiricos-R/Topics.txt"
dicionario = Counter()

with open(arquivo,"r") as dados:
    texto = dados.read()
    ltextos = texto.replace("<top>","").split("</top>")
    #ltextos = [elem.split("<title> ")[1] for elem in ltextos]
    bloblist = [tb(elem) for elem in ltextos]

    for i, blob in enumerate(bloblist):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:3]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))