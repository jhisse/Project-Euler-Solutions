#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
    Author: José Vitor Hisse & Ana Clara Salgueiro
    Date: 10/09/2016
    Python Version: 3.6
"""


def maior_primo(n):

    maior_divisor = 0
    divisor_atual = 2
    while divisor_atual < n:
        if n % divisor_atual == 0:
            maior_divisor = divisor_atual
            n = n / divisor_atual
        else:
            divisor_atual += 1
    return divisor_atual

print(maior_primo(600851475143))
