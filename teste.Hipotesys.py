# -*- coding: utf-8 -*-

import random

import scipy

salarios = list(range(4800,7200))

datasciente = []

for i in range(1000):
    datasciente.append(random.choice(salarios))
    
scipy.stats.norm()
