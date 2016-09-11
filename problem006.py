#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
    Author: José Vitor Hisse
    Date: 10/09/2016
    Python Version: 3.6
"""


def diferenca(n):
    n = n + 1
    soma_dos_quadrados = sum([x ** 2 for x in range(n)])
    quadrado_da_soma = sum([x for x in range(n)]) ** 2
    return quadrado_da_soma - soma_dos_quadrados


print(diferenca(100))
