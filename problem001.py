# -*- coding: utf-8 -*-

"""
   Author: José Vitor Hisse
   Date: 10/09/2016
   Python Version: 3.6
"""


# Função que retorna a soma de todos os multiplos de 3 e 5 abaixo do numero n
def soma_multiplos3e5(n):
    return sum([i for i in range(1, n) if i % 3 == 0 or i % 5 == 0])


print(soma_multiplos3e5(1000))
