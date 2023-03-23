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
df = pd.read_excel("Vanillin Data.xlsx", sheet_name = "Bond lengths", index_col = "Functional")

dffuncopt = df.iloc[0:7, 0:11]
dffuncopt = dffuncopt.astype(float)
dffuncopt = round(dffuncopt, 3)

dffuncopterr = df.iloc[0:6, 11:14]
dffuncopterr = dffuncopterr.astype(float)
dffuncopterr = round(dffuncopterr, 3)

dfbondopt = df.iloc[8:19, 0:11]
dfbondopt = dfbondopt.astype(float)
dfbondopt = round(dfbondopt, 3)

dfbondopterr = df.iloc[8:19, 11:14]
dfbondopterr = dfbondopterr.astype(float)
dfbondopterr = round(dfbondopterr, 3)

dffuncexp = df.iloc[0:7, 14:25]
dffuncexp = dffuncexp.astype(float)
dffuncexp = round(dffuncexp, 3)

dffuncexperr = df.iloc[0:6, 25:28]
dffuncexperr = dffuncexperr.astype(float)
dffuncexperr = round(dffuncexperr, 3)

dfbondexp = df.iloc[8:19, 14:25]
dfbondexp = dfbondexp.astype(float)
dfbondexp = round(dfbondexp, 3)

dfbondexperr = df.iloc[8:19, 25:28]
dfbondexperr = dfbondexperr.astype(float)
dfbondexperr = round(dfbondexperr, 3)

###############################################################################
#Plot
###############################################################################
######################
#Optimised structures#
######################
#Add plot
fig1, ax = plt.subplots(figsize = (20,10))

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
fig1.tight_layout()

#Create subplots
sub1 = fig1.add_subplot(3, 3, (1, 3))
sub2 = fig1.add_subplot(3, 3, (4, 6))
sub3 = fig1.add_subplot(3, 3, (7, 9))

#Create barcharts
#############
#Bar chart 1#
#############
x1opt = np.arange(0, 55, 5) + 3.5

y1optBP86 = dffuncopt.iloc[0,:]
y1optPBE0 = dffuncopt.iloc[1,:]
y1optB3LYP = dffuncopt.iloc[2,:]
y1optM06 = dffuncopt.iloc[5,:]
y1optM062X = dffuncopt.iloc[3,:]
y1optwB97XD = dffuncopt.iloc[4,:]
y1optExpt = dffuncopt.iloc[6,:]

bar1optBP86 = sub1.bar(x1opt - 1.5, y1optBP86, 0.5, color = "black")
bar1optPBE0 = sub1.bar(x1opt - 1, y1optPBE0, 0.5, color = "blue")
bar1optB3LYP = sub1.bar(x1opt - 0.5, y1optB3LYP, 0.5, color = "green")
bar1optM062X = sub1.bar(x1opt, y1optM062X, 0.5, color = "pink")
bar1optwB97XD = sub1.bar(x1opt + 0.5, y1optwB97XD, 0.5, color = "purple")
bar1optM06 = sub1.bar(x1opt + 1, y1optM06, 0.5, color = "orange")
bar1optExpt = sub1.bar(x1opt + 1.5, y1optExpt, 0.5, color = "red", edgecolor = "black", linewidth = 1, hatch = "///")

sub1.bar_label(bar1optBP86, rotation = 90, padding = 8, color = "black", fontsize = 14)
sub1.bar_label(bar1optPBE0, rotation = 90, padding = 8, color = "blue", fontsize = 14)
sub1.bar_label(bar1optB3LYP, rotation = 90, padding = 8, color = "green", fontsize = 14)
sub1.bar_label(bar1optM062X, rotation = 90, padding = 8, color = "pink", fontsize = 14)
sub1.bar_label(bar1optwB97XD, rotation = 90, padding = 8, color = "purple", fontsize = 14)
sub1.bar_label(bar1optM06, rotation = 90, padding = 8, color = "orange", fontsize = 14)
sub1.bar_label(bar1optExpt, rotation = 90, padding = 8, color = "red", fontsize = 14)

#############
#Bar chart 2#
#############
x2opt = np.arange(0, 30, 5) + 2

y2optMSD = dffuncopterr.iloc[0:6, 0]
y2optMAD = dffuncopterr.iloc[0:6, 1]
y2optSTD = dffuncopterr.iloc[0:6, 2]

bar2optMSD = sub2.bar(x2opt - 0.5, y2optMSD, 0.5, color = "teal")
bar2optMAD = sub2.bar(x2opt, y2optMAD, 0.5, color = "maroon")
bar2optSTD = sub2.bar(x2opt + 0.5, y2optSTD, 0.5, color = "dimgrey")

sub2.bar_label(bar2optMSD, rotation = 90, padding = 5, color = "teal", fontsize = 14)
sub2.bar_label(bar2optMAD, rotation = 90, padding = 5, color = "maroon", fontsize = 14)
sub2.bar_label(bar2optSTD, rotation = 90, padding = 5, color = "dimgrey", fontsize = 14)

#############
#Bar chart 3#
#############
x3opt = np.arange(0, 55, 5) + 2

y3optMSD = dfbondopterr.iloc[0:11, 0]
y3optMAD = dfbondopterr.iloc[0:11, 1]
y3optSTD = dfbondopterr.iloc[0:11, 2]

bar3optMSD = sub3.bar(x3opt - 0.5, y3optMSD, 0.5, color = "teal")
bar3optMAD = sub3.bar(x3opt, y3optMAD, 0.5, color = "maroon")
bar3optSTD = sub3.bar(x3opt + 0.5, y3optSTD, 0.5, color = "dimgrey")
sub3.plot([0, 57], [0,0], color = "black", linewidth = 1)

sub3.bar_label(bar3optMSD, rotation = 90, padding = 5, color = "teal", fontsize = 14)
sub3.bar_label(bar3optMAD, rotation = 90, padding = 5, color = "maroon", fontsize = 14)
sub3.bar_label(bar3optSTD, rotation = 90, padding = 5, color = "dimgrey", fontsize = 14)

#Limits
sub1.set_xlim([0 ,57])
sub1.set_ylim([1.15, 1.75])
sub1.set_ylabel("Bond length (Å)")

sub2.set_ylim([0, 0.025])
sub2.set_xlim([0 ,29])
sub2.set_ylabel("Deviation (Å)")

sub3.set_xlim([0 ,55])
sub3.set_ylim([-0.032, 0.037])
sub3.set_ylabel("Deviation (Å)")

#Ticks
sub1.set_xticks(x1opt)
sub1.set_xticklabels(["C-C$_{Ar (1)}$", "C-C$_{Ar (2)}$", "C-C$_{Ar (3)}$", "C-C$_{Ar (4)}$", "C-C$_{Ar (5)}$", "C-C$_{Ar (6)}$", "C-C$_{Ald}$", "C-OH", "C$_{Ald}$=O", "C$_{Ar}$-O", "C$_{Alk}$-O"])

sub2.set_xticks(x2opt)
sub2.set_xticklabels(["BP86", "PBE0", "B3LYP", "M06-2X", "wB97XD", "M06"])

sub3.set_xticks(x3opt)
sub3.set_xticklabels(["C-C$_{Ar (1)}$", "C-C$_{Ar (2)}$", "C-C$_{Ar (3)}$", "C-C$_{Ar (4)}$", "C-C$_{Ar (5)}$", "C-C$_{Ar (6)}$", "C-C$_{Ald}$", "C-OH", "C$_{Ald}$=O", "C$_{Ar}$-O", "C$_{Alk}$-O"])

#Legends
BP86leg = plt.Rectangle((0,0),1,0.025, color = "black", label = "BP86")
PBE0leg = plt.Rectangle((0,0),1,0.025, color = "blue", label = "PBE0")
B3LYPleg = plt.Rectangle((0,0),1,0.025, color = "green", label = "B3LYP")
M062Xleg = plt.Rectangle((0,0),1,0.025, color = "pink", label = "M06-2X")
wB97XDleg = plt.Rectangle((0,0),1,0.025, color = "purple", label = "wB97XD")
M06leg = plt.Rectangle((0,0),1,0.025, color = "orange", label = "M06")
Exptleg = plt.Rectangle((0,0),1,0.025, label = "Expt", facecolor = "red", edgecolor = "black", hatch = "///")
legends1opt = (BP86leg, PBE0leg, B3LYPleg, M062Xleg, wB97XDleg, M06leg, Exptleg)

sub1.legend(handles=legends1opt, loc="upper right", ncol=7)

MSDleg = plt.Rectangle((0,0),1,0.025, color = "teal", label = "MSD")
MADleg = plt.Rectangle((0,0),1,0.025, color = "maroon", label = "MAD")
STDleg = plt.Rectangle((0,0),1,0.025, color = "dimgrey", label = "STD")
legends2opt = (MSDleg, MADleg, STDleg)

sub2.legend(handles=legends2opt, loc="upper right", ncol=3)

sub3.legend(handles=legends2opt, loc="lower left", ncol=3)

#Save figure
fig1.savefig("Geometry optimised bond lengths.png", format = "png", bbox_inches='tight', dpi = 300)
plt.show 

#########################
#Experimental structures#
#########################
#Add plot
fig2, ax = plt.subplots(figsize = (20,10))

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
fig2.tight_layout()

#Create subplots
sub4 = fig2.add_subplot(3, 3, (1, 3))
sub5 = fig2.add_subplot(3, 3, (4, 6))
sub6 = fig2.add_subplot(3, 3, (7, 9))

#Create barcharts
#############
#Bar chart 4#
#############
x1exp = np.arange(0, 55, 5) + 3.5

y1expBP86 = dffuncexp.iloc[0,:]
y1expPBE0 = dffuncexp.iloc[1,:]
y1expB3LYP = dffuncexp.iloc[2,:]
y1expM06 = dffuncexp.iloc[5,:]
y1expM062X = dffuncexp.iloc[3,:]
y1expwB97XD = dffuncexp.iloc[4,:]
y1expExpt = dffuncexp.iloc[6,:]

bar1expBP86 = sub4.bar(x1exp - 1.5, y1expBP86, 0.5, color = "black")
bar1expPBE0 = sub4.bar(x1exp - 1, y1expPBE0, 0.5, color = "blue")
bar1expB3LYP = sub4.bar(x1exp - 0.5, y1expB3LYP, 0.5, color = "green")
bar1expM062X = sub4.bar(x1exp, y1expM062X, 0.5, color = "pink")
bar1expwB97XD = sub4.bar(x1exp + 0.5, y1expwB97XD, 0.5, color = "purple")
bar1expM06 = sub4.bar(x1exp + 1, y1expM06, 0.5, color = "orange")
bar1expExpt = sub4.bar(x1exp + 1.5, y1expExpt, 0.5, color = "red", edgecolor = "black", linewidth = 1, hatch = "///")

sub4.bar_label(bar1expBP86, rotation = 90, padding = 8, color = "black", fontsize = 14)
sub4.bar_label(bar1expPBE0, rotation = 90, padding = 8, color = "blue", fontsize = 14)
sub4.bar_label(bar1expB3LYP, rotation = 90, padding = 8, color = "green", fontsize = 14)
sub4.bar_label(bar1expM062X, rotation = 90, padding = 8, color = "pink", fontsize = 14)
sub4.bar_label(bar1expwB97XD, rotation = 90, padding = 8, color = "purple", fontsize = 14)
sub4.bar_label(bar1expM06, rotation = 90, padding = 8, color = "orange", fontsize = 14)
sub4.bar_label(bar1expExpt, rotation = 90, padding = 8, color = "red", fontsize = 14)

#############
#Bar chart 5#
#############
x2exp = np.arange(0, 30, 5) + 2

y2expMSD = dffuncexperr.iloc[0:6, 0]
y2expMAD = dffuncexperr.iloc[0:6, 1]
y2expSTD = dffuncexperr.iloc[0:6, 2]

bar2expMSD = sub5.bar(x2exp - 0.5, y2expMSD, 0.5, color = "teal")
bar2expMAD = sub5.bar(x2exp, y2expMAD, 0.5, color = "maroon")
bar2expSTD = sub5.bar(x2exp + 0.5, y2expSTD, 0.5, color = "dimgrey")

sub5.bar_label(bar2expMSD, rotation = 90, padding = 5, color = "teal", fontsize = 14)
sub5.bar_label(bar2expMAD, rotation = 90, padding = 5, color = "maroon", fontsize = 14)
sub5.bar_label(bar2expSTD, rotation = 90, padding = 5, color = "dimgrey", fontsize = 14)

#############
#Bar chart 6#
#############
x3exp = np.arange(0, 55, 5) + 2

y3expMSD = dfbondexperr.iloc[0:11, 0]
y3expMAD = dfbondexperr.iloc[0:11, 1]
y3expSTD = dfbondexperr.iloc[0:11, 2]

bar3expMSD = sub6.bar(x3exp - 0.5, y3expMSD, 0.5, color = "teal")
bar3expMAD = sub6.bar(x3exp, y3expMAD, 0.5, color = "maroon")
bar3expSTD = sub6.bar(x3exp + 0.5, y3expSTD, 0.5, color = "dimgrey")
sub6.plot([0, 57], [0,0], color = "black", linewidth = 1)

sub6.bar_label(bar3expMSD, rotation = 90, padding = 5, color = "teal", fontsize = 14)
sub6.bar_label(bar3expMAD, rotation = 90, padding = 5, color = "maroon", fontsize = 14)
sub6.bar_label(bar3expSTD, rotation = 90, padding = 5, color = "dimgrey", fontsize = 14)

#Limits
sub4.set_xlim([0 ,57])
sub4.set_ylim([1.15, 1.75])
sub4.set_ylabel("Bond length (Å)")

sub5.set_ylim([0, 0.04])
sub5.set_xlim([0 ,29])
sub5.set_ylabel("Deviation (Å)")

sub6.set_xlim([0 ,55])
sub6.set_ylim([-0.032, 0.034])
sub6.set_ylabel("Deviation (Å)")

#Ticks
sub4.set_xticks(x1exp)
sub4.set_xticklabels(["C-C$_{Ar (1)}$", "C-C$_{Ar (2)}$", "C-C$_{Ar (3)}$", "C-C$_{Ar (4)}$", "C-C$_{Ar (5)}$", "C-C$_{Ar (6)}$", "C-C$_{Ald}$", "C-OH", "C$_{Ald}$=O", "C$_{Ar}$-O", "C$_{Alk}$-O"])

sub5.set_xticks(x2exp)
sub5.set_xticklabels(["BP86", "PBE0", "B3LYP", "M06-2X", "wB97XD", "M06"])

sub6.set_xticks(x3exp)
sub6.set_xticklabels(["C-C$_{Ar (1)}$", "C-C$_{Ar (2)}$", "C-C$_{Ar (3)}$", "C-C$_{Ar (4)}$", "C-C$_{Ar (5)}$", "C-C$_{Ar (6)}$", "C-C$_{Ald}$", "C-OH", "C$_{Ald}$=O", "C$_{Ar}$-O", "C$_{Alk}$-O"])

#Legends
BP86leg = plt.Rectangle((0,0),1,0.025, color = "black", label = "BP86")
PBE0leg = plt.Rectangle((0,0),1,0.025, color = "blue", label = "PBE0")
B3LYPleg = plt.Rectangle((0,0),1,0.025, color = "green", label = "B3LYP")
M062Xleg = plt.Rectangle((0,0),1,0.025, color = "pink", label = "M06-2X")
wB97XDleg = plt.Rectangle((0,0),1,0.025, color = "purple", label = "wB97XD")
M06leg = plt.Rectangle((0,0),1,0.025, color = "orange", label = "M06")
Exptleg = plt.Rectangle((0,0),1,0.025, label = "Expt", facecolor = "red", edgecolor = "black", hatch = "///")
legends1exp = (BP86leg, PBE0leg, B3LYPleg, M062Xleg, wB97XDleg, M06leg, Exptleg)

sub4.legend(handles=legends1exp, loc="upper right", ncol=7)

MSDleg = plt.Rectangle((0,0),1,0.025, color = "teal", label = "MSD")
MADleg = plt.Rectangle((0,0),1,0.025, color = "maroon", label = "MAD")
STDleg = plt.Rectangle((0,0),1,0.025, color = "dimgrey", label = "STD")
legends2exp = (MSDleg, MADleg, STDleg)

sub5.legend(handles=legends2exp, loc="upper right", ncol=3)

sub6.legend(handles=legends2exp, loc="lower left", ncol=3)

#Save figure
fig2.savefig("Experimental optimised bond lengths.png", format = "png", bbox_inches='tight', dpi = 300)
plt.show 