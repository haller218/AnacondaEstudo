# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:43:44 2019

@author: eliseu.lucena
"""

import math

from scipy.stats import binom


def permutation ( primary, second) :
    
    return math.factorial(primary) / math.factorial(second) / \
                    math.factorial(primary - second)



def distributionDiscritive ( valor = 3, probabilidade = 0.5, lances = 5) :
    
    return math.pow(probabilidade, valor) * permutation (lances, valor) * \
                         pow((1 - probabilidade),(lances - valor))
        
        
    
def testeDataAcomulationProbability (  ) :
    
    acumulado = binom.cdf(3,5,0.5) # acomulado q1~3
    
    



def hellworld (  ) :

    print ( "Hello, World!" )
    
    
    
def testeSomatorio (  ) :
    
    somatorio = 0
    
    for i in range (0,5):
        somatorio += distributionDiscritive(i,0.25,4)
        
    print (binom.pmf(2,4,0.5))
    
    print (binom.cdf(4,4,0.25))
    
    print (binom.pmf(7,12,0.25) * 100)
    
    print (binom.pmf(12,12,0.25) * 100)
    
    print (somatorio)
    
    
    
def probabilitDataRow (  ) :
    
    consta = 10
    
    print ("probabilit : ")
    
    probabilit = 0.5
    
    somatorio = 0
    
    for i in range(consta+1):
        
        
        aux = binom.pmf(i,consta,probabilit)
        
        somatorio += aux
        
        print ( "{0:>3} => {1}".format(i, consta), end=' ' )
        
        print ( "{0:>20.4f}".format( aux*100 ))
    
    
    
    print (somatorio)
    
    

def data_liner_regresion_matlab (  ) :
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    
    
    
    
def main (  ) :
    
    # probabilitDataRow (  )
    
    data_liner_regresion_matlab (  )
    
    
if __name__ == "__main__":
    main (  )
