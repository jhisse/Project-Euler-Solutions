#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
    Author: José Vitor Hisse & Ana Clara Salgueiro
    Date: 10/09/2016
    Python Version: 3.6
"""


# n é igual o numero de digitos de cada fator
def palindromic(n):
    maior_fator = "9" * n
    menor_fator = "1" + "0" * int(n - 1)
    maior_fator = int(maior_fator)
    menor_fator = int(menor_fator)
    fatores = list(range(maior_fator, menor_fator - 1, -1))
    palindromo = []
    for i in fatores:
        for j in fatores:
            conferir = str(i * j)
            reverso = conferir[::-1]
            if conferir == reverso:
                palindromo.append(int(conferir))
    palindromo = set(palindromo)
    maior = max(palindromo)
    return maior


print(palindromic(3))
