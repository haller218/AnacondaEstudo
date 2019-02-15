# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:46:07 2019

@author: eliseu.lucena
"""

import numpy as np

from scipy import stats

jogadores = [40000,18000,12000,250000,30000,140000,300000,40000,800000]


np.mean(jogadores)

np.median(jogadores)

quantile = np.quantile(jogadores)

np.std(jogadores)

stats.describe (jogadores)
