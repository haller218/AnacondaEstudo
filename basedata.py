# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import pandas as pd

import numpy as np

base = pd.read_csv("iris.csv")

base

np.random.seed(218325)
amostra = np.random.choice(a = [1,0], size=150,replace = True,
                           p = [0.5,0.5])

amostra2 = np.random.choice(a = [1,0], size=800050,replace = True,
                           p = [0.5,0.5])


lenf = len(amostra)

fre1 = (len(amostra[amostra == 1]))
fre0 = (len(amostra[amostra == 0]))

fra1 = (len(amostra2[amostra2 == 1]))
fra0 = (len(amostra2[amostra2 == 0]))


print ( "Amostra 1" )
print ("probabilidade de aparecer 0 " ,(fre1 / len(amostra) * 100))
print ("probabilidade de aparecer 1 " ,(fre0 / len(amostra) * 100))


print ( "Amostra 2" )
print ("probabilidade de aparecer 0 " ,(fra1 / len(amostra2) * 100))
print ("probabilidade de aparecer 1 " ,(fra0 / len(amostra2) * 100))


