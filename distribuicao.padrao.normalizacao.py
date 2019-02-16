# -*- coding: utf-8 -*-

from scipy.stats import norm


# conjunto de objetos em uma cesta, a media é 8 e o desvio padrão é 2
# Qual a probabilidade de tirar um objeto com peso menor que 6 quilos?


proba = norm.cdf(6,8,2)

print ( proba )

# qual a probabilidade de tirar um objeto com um peso maior que 6 quilos? 

proba = 1 - norm.cdf(6,8,2)

proba = norm.sf(6,8,2)

print ( proba )

# qual a probabilidade de tirar um objeto que o peso é menor do que 6 e maior 
# que 10 quilos ?


proba = norm.cdf(6,8,2) + norm.sf(10,8,2)

print ( proba )

# qual a probabilidade de tirar um objeto que o peso é menor do que 10 e maior 
# que 8 quilos ?

proba = norm.cdf(10,8,2) - norm.cdf(8,8,2)

print ( proba )
