# -*- coding: utf-8 -*-

from scipy.stats import t

# media do salario do cientista de dados = R$ 75,00 por hora
# Amostra de 9 funcionarios e desvio padrao = 10

# qual a probabilidade de selecionar um scientista de dados e o
# salario se menor que R$ 80,00 por hora

t.cdf(1.5,8)

# qual a probabilidade do salario ser maior que R$ 80,00 por hora

t.sf(1.5,8) * 100

t.sf(1.5,8) + t.cdf(1.5,8)
t.cdf(1.5,8) + 1-t.cdf(1.5,8)
