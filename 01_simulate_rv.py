#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:09:19 2021

@author: Eduardo Cuéllar
"""
import pandas as pd
import numpy as np
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2

print("Hello word!")

nb_sims=10**6
df=9
dist_name='chi-square'#student normal exponential uniform chi-square
if dist_name=='normal':
    x=np.random.standard_normal(nb_sims)
    x_str=dist_name
elif dist_name=='exponential':
    x=np.random.standard_exponential(nb_sims)
    x_str=dist_name
elif dist_name=='uniform':
    x=np.random.uniform(0,1,nb_sims)
    x_str=dist_name
elif dist_name=='student':
    x=np.random.standard_t(df=df,size=nb_sims)
    x_str=dist_name+ ' / df= '+str(df)
elif dist_name=='chi-square':
    x=np.random.chisquare(df=df,size=nb_sims)
    x_str=dist_name+ ' / df= '+str(df)
#plot histogram
plt.figure()
plt.hist(x,bins=100)
plt.title(x_str)
plt.show()