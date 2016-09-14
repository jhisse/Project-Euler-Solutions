# coding: utf-8

'''
    Author: José Vitor Hisse
    Python Version: 3.5
'''

n = list(range(1,21))
inicio = 20
while True:
    divisores = 0
    for i in n:
        if inicio%i == 0:
            divisores +=1
    if divisores == len(n):
        break
    else:
        inicio += 10
print(inicio)