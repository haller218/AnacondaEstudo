# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:25:00 2019

@author: eliseu.lucena
"""

import pandas as pd

import numpy as np

from math import ceil

def media ( lista_valores ) :
    
    tamanho = len ( lista_valores )
    
    acumulador = 0
    
    for i in range(len(lista_valores))  :
        
        acumulador += lista_valores[i]
        
    acumulador /= tamanho
        
    
    
    
def mediana ( lista_valores = [1,2,3,4,5,6,7,8,9,10] ) : 
    
    lista_valores.sort()
    
    
    
    
    
def varianca (  ) :
        
    print ("asdf")
    
    

def main (  ) :
    
    populacao = 150
    
    amostra = 14
    
    k = ceil(populacao / amostra)
    
    # np.random.seed(1562103)
    r = np.random.randint(low = 1, high = k + 1, size = 1)
    
    # list(range(1,populacao + 1)).index(*(r))
    
    acumulador = r[0]
    
    sorteados = []
    
    for i in range (amostra):
        
        sorteados.append(acumulador)
        
        acumulador += k
    
    
    base = pd.read_csv("iris.csv")
    
    base_final = base.loc[sorteados]
    
    media ( base_final )
    
    
    
if __name__ == "__main__":
    main (  )
