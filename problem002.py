#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
   Author: José Vitor Hisse
   Date: 10/09/2016
   Python Version: 3.6
"""


# Soma termos pares de fibonacci cuja soma não exceda n
def soma_fibonacci_pares(n):
    termo1 = 0
    termo2 = 1
    termo3 = 1
    # Armazena a soma dos termos pares da sequência
    soma_pares = 0
    # Executa o loop enquanto a soma dos pares seja menor que n
    while soma_pares + termo3 < n:
        termo3 = termo1 + termo2
        if (termo3 % 2 == 0):
            soma_pares += termo3
        else:
            pass
        termo1 = termo2
        termo2 = termo3
    return soma_pares


print(soma_fibonacci_pares(4000000))
