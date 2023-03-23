# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:09:48 2023

@author: 2811088N
"""

###############################################################################
#Libraries
###############################################################################
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib import cbook
from matplotlib.patches import ConnectionPatch

#Read data for expt 
df = pd.read_excel("Vanillin Data.xlsx", sheet_name = "Expt")

#Organise Dataframe
df = df.astype(float)
df = df.round(decimals=1)
df = df * -0.04

#Create x and y lists
xexpt = np.arange(450,3970,4)
xexpt = xexpt.tolist()
yexpt = pd.Series(df["A"]).to_list()

#Smoothen out weird drift and set baseline below 0
xexpt = [round(elem, 1) for elem in xexpt]
yexpt = [round(elem, 1) for elem in yexpt]
yexpt = [elem-2 for elem in yexpt]

#Plot font
plt.rcParams['font.family'] = "serif"
plt.rcParams.update({'font.size': 18})

fig, ax = plt.subplots(figsize=(20,10))
plt.plot(xexpt, yexpt, c = "red")

ax.set_xlim([3966,450])
ax.set_yticks([])

ax.set_xlabel("Wavenumber ($\mathregular{cm^{-1}}$)")
ax.set_ylabel("Transmittance")

fig.savefig("Expt spectrui.png", format = "png", bbox_inches='tight', dpi = 300)
plt.show    
