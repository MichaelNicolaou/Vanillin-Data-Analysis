# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 14:39:02 2023

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

###############################################################################
#Data process
###############################################################################
#Spreadsheet selection
#Read data   
df = pd.read_excel("Vanillin Data.xlsx", sheet_name = "IR Spectra", index_col = "Functional")
# df = df.astype(float)
# df = round(df, 1)

dffunc = df.iloc[0:7, 0:8]
dffunc = dffunc.astype(float)
dffunc = round(dffunc, 1)
dffuncerr = df.iloc[0:6, 8:11]
dffuncerr = dffuncerr.astype(float)
dffuncerr = round(dffuncerr, 1)
dfpeak = df.iloc[8:16, 0:7]
dfpeak = dfpeak.astype(float)
dfpeak = round(dfpeak, 1)
dfpeakerr = df.iloc[8:16, 7:10]
dfpeakerr = dfpeakerr.astype(float)
dfpeakerr = round(dfpeakerr, 1)

###############################################################################
#Plot
###############################################################################
#############
#Functionals#
#############
#Add plot
fig, ax = plt.subplots(figsize = (20,10))

#Plot font
plt.rcParams['font.family'] = "serif"
plt.rcParams.update({'font.size': 18})

#Remove main plot default axis ticks
plt.yticks([])
plt.xticks([])

#Remove main plot frame
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

#Adjust subplot positions
plt.subplots_adjust(bottom = -0.2, left = 0, top = 1., right = 1)
fig.tight_layout()

#Create subplots
sub1 = fig.add_subplot(3, 3, (1, 3))
sub2 = fig.add_subplot(3, 3, (4, 6))
sub3 = fig.add_subplot(3, 3, (7, 9))

#Create barcharts
#############
#Bar chart 1#
#############
x1 = np.arange(0, 40, 5) + 3.5

y1BP86 = dffunc.iloc[0,:]
y1PBE0 = dffunc.iloc[1,:]
y1B3LYP = dffunc.iloc[2,:]
y1M06 = dffunc.iloc[5,:]
y1M062X = dffunc.iloc[3,:]
y1wB97XD = dffunc.iloc[4,:]
y1Expt = dffunc.iloc[6,:]

bar1BP86 = sub1.bar(x1 - 1.5, y1BP86, 0.5, color = "black")
bar1PBE0 = sub1.bar(x1 - 1, y1PBE0, 0.5, color = "blue")
bar1B3LYP = sub1.bar(x1 - 0.5, y1B3LYP, 0.5, color = "green")
bar1M062X = sub1.bar(x1, y1M062X, 0.5, color = "pink")
bar1wB97XD = sub1.bar(x1 + 0.5, y1wB97XD, 0.5, color = "purple")
bar1M06 = sub1.bar(x1 + 1, y1M06, 0.5, color = "orange")
bar1Expt = sub1.bar(x1 + 1.5, y1Expt, 0.5, color = "red", edgecolor = "black", linewidth = 1, hatch = "///")

sub1.bar_label(bar1BP86, rotation = 90, padding = 8, color = "black", fontsize = 14)
sub1.bar_label(bar1PBE0, rotation = 90, padding = 8, color = "blue", fontsize = 14)
sub1.bar_label(bar1B3LYP, rotation = 90, padding = 8, color = "green", fontsize = 14)
sub1.bar_label(bar1M062X, rotation = 90, padding = 8, color = "pink", fontsize = 14)
sub1.bar_label(bar1wB97XD, rotation = 90, padding = 8, color = "purple", fontsize = 14)
sub1.bar_label(bar1M06, rotation = 90, padding = 8, color = "orange", fontsize = 14)
sub1.bar_label(bar1Expt, rotation = 90, padding = 8, color = "red", fontsize = 14)

#############
#Bar chart 2#
#############
x2 = np.arange(0, 30, 5) + 2

y2MSD = dffuncerr.iloc[0:6, 0]
y2MAD = dffuncerr.iloc[0:6, 1]
y2STD = dffuncerr.iloc[0:6, 2]

bar2MSD = sub2.bar(x2 - 0.5, y2MSD, 0.5, color = "teal")
bar2MAD = sub2.bar(x2, y2MAD, 0.5, color = "maroon")
bar2STD = sub2.bar(x2 + 0.5, y2STD, 0.5, color = "dimgrey")

sub2.bar_label(bar2MSD, rotation = 90, padding = 5, color = "teal", fontsize = 14)
sub2.bar_label(bar2MAD, rotation = 90, padding = 5, color = "maroon", fontsize = 14)
sub2.bar_label(bar2STD, rotation = 90, padding = 5, color = "dimgrey", fontsize = 14)

#############
#Bar chart 3#
#############
x3 = np.arange(0, 40, 5) + 2

y3MSD = dfpeakerr.iloc[0:8, 0]
y3MAD = dfpeakerr.iloc[0:8, 1]
y3STD = dfpeakerr.iloc[0:8, 2]

bar3MSD = sub3.bar(x3 - 0.5, y3MSD, 0.5, color = "teal")
bar3MAD = sub3.bar(x3, y3MAD, 0.5, color = "maroon")
bar3STD = sub3.bar(x3 + 0.5, y3STD, 0.5, color = "dimgrey")

sub3.bar_label(bar3MSD, rotation = 90, padding = 5, color = "teal", fontsize = 14)
sub3.bar_label(bar3MAD, rotation = 90, padding = 5, color = "maroon", fontsize = 14)
sub3.bar_label(bar3STD, rotation = 90, padding = 5, color = "dimgrey", fontsize = 14)

#Limits
sub1.set_xlim([0 ,42])
sub1.set_ylim([1000, 4800])
sub1.set_ylabel("Wavenumber (cm$^{-1}$)")

sub2.set_ylim([0, 325])
sub2.set_xlim([0 ,29])
sub2.set_ylabel("Deviation (cm$^{-1}$)")

sub3.set_ylim([0, 305])
sub3.set_xlim([0 ,39])
sub3.set_ylabel("Deviation (cm$^{-1}$)")

#Ticks
sub1.set_xticks(x1)
sub1.set_xticklabels(["O-H", "C$_{Ar}$-H$_{(3)}$", "C$_{Ar}$-H$_{(2)}$", "C$_{Ar}$-H$_{(1)}$", "C$_{Alk}$-H", "C$_{Ald}$-H", "C$_{Ald}$=O", "C$_{Ar}$-O"])

sub2.set_xticks(x2)
sub2.set_xticklabels(["BP86", "PBE0", "B3LYP", "M06-2X", "wB97XD", "M06"])

sub3.set_xticks(x3)
sub3.set_xticklabels(["O-H", "C$_{Ar}$-H$_{(3)}$", "C$_{Ar}$-H$_{(2)}$", "C$_{Ar}$-H$_{(1)}$", "C$_{Alk}$-H", "C$_{Ald}$-H", "C$_{Ald}$=O", "C$_{Ar}$-O"])

#Legends
BP86leg = plt.Rectangle((0,0),1,0.025, color = "black", label = "BP86")
PBE0leg = plt.Rectangle((0,0),1,0.025, color = "blue", label = "PBE0")
B3LYPleg = plt.Rectangle((0,0),1,0.025, color = "green", label = "B3LYP")
M062Xleg = plt.Rectangle((0,0),1,0.025, color = "pink", label = "M06-2X")
wB97XDleg = plt.Rectangle((0,0),1,0.025, color = "purple", label = "wB97XD")
M06leg = plt.Rectangle((0,0),1,0.025, color = "orange", label = "M06")
Exptleg = plt.Rectangle((0,0),1,0.025, label = "Expt", facecolor = "red", edgecolor = "black", hatch = "///")
legends1 = (BP86leg, PBE0leg, B3LYPleg, M062Xleg, wB97XDleg, M06leg, Exptleg)

sub1.legend(handles=legends1, loc="upper right", ncol=7)

MSDleg = plt.Rectangle((0,0),1,0.025, color = "teal", label = "MSD")
MADleg = plt.Rectangle((0,0),1,0.025, color = "maroon", label = "MAD")
STDleg = plt.Rectangle((0,0),1,0.025, color = "dimgrey", label = "STD")
legends2 = (MSDleg, MADleg, STDleg)

sub2.legend(handles=legends2, loc="upper right", ncol=3)

sub3.legend(handles=legends2, loc="upper right", ncol=3)

#Save figure
fig.savefig("IR spectra barcharts.png", format = "png", bbox_inches='tight', dpi = 300)
plt.show 

