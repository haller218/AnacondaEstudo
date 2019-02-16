# -*- coding: utf-8 -*-

from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt


data = norm.rvs(size=1000)

stats.probplot(data, plot=plt)


stats.shapiro(data)
