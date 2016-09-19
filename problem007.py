# coding: utf-8

'''
    Author: José Vitor Hisse
    Python Version: 3.5
'''

primos = [2]
n = 2
fim = 10001
while True:
    primo = 1
    for i in primos:
        if n % i == 0:
            primo = 0
            break
    if primo == 1:
        primos.append(n)
    if len(primos) == fim:
        break
    n += 1
print(n)