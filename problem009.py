# coding: utf-8

'''
    Author: José Vitor Hisse
    Python Version: 3.5
'''

n = 1000
condicao = False
for i in range(1, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if i + j + k == 1000 and i ** 2 + j ** 2 == k ** 2:
                print(i * j * k)
                condicao = True
                break
        if condicao:
            break
    if condicao:
        break
