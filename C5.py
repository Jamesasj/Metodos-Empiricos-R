#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:34:10 2018

@author: james
"""

from collections import Counter


def vetorizar(texto):
    return texto.replace(',','').replace('.','').replace(':','').replace(';','').replace('!','').replace('?','').lower().split()

arquivo = "/home/james/Documentos/Metodos-Empiricos-R/Topics.txt"
dicionario = Counter()

with open(arquivo,"r") as dados:
    texto = dados.read()
    ltextos = texto.replace("<top>","").split("</top>")
    #ltextos = [elem.split("<title> ")[1] for elem in ltextos]
    
    for texto in ltextos:
        lwords = vetorizar(texto)
        for word in lwords:
            dicionario[word] +=1