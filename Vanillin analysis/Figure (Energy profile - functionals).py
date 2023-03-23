# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:14:10 2023

@author: Micha
"""

###############################################################################
#Libraries
###############################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

###############################################################################
#Data process
###############################################################################
#Read excel spreadsheet
df = pd.read_excel("Vanillin Data.xlsx", sheet_name="Gibbs (Gas)", index_col="Functional")

#Slice spreadsheet into individual functionals
dfBP86 = df.iloc[1:8, 1:15]
dfPBE0 = df.iloc[9:16, 1:15]
dfB3LYP = df.iloc[17:24, 1:15]
dfM062X = df.iloc[25:32, 1:15]
dfwB97XD = df.iloc[33:40, 1:15]
dfM06 = df.iloc[41:48, 1:15]

#Equation for element-wise multiplication (coefficient * energy of molecule)
def Gibbs_step(x, y):
    G = x*y
    return sum(G)


################################################################################
#Databases
################################################################################
######
#BP86#
######
#Collect each step as a list of coefficients and the energies as a seperate list
step_1_BP86 = pd.to_numeric(dfBP86.iloc[0, :])
step_2_BP86 = pd.to_numeric(dfBP86.iloc[1, :])
step_3_BP86 = pd.to_numeric(dfBP86.iloc[2, :])
step_4_BP86 = pd.to_numeric(dfBP86.iloc[3, :])
step_5_BP86 = pd.to_numeric(dfBP86.iloc[4, :])
# BP86energy = pd.to_numeric(dfBP86.iloc[5, :])
BP86energy = pd.to_numeric(dfBP86.iloc[6, :])

#Find relative energy level for each reaction step
BP86G = Gibbs_step(step_1_BP86, BP86energy)
BP86G1 = (Gibbs_step(step_1_BP86, BP86energy)) - BP86G
BP86G2 = Gibbs_step(step_2_BP86, BP86energy) - BP86G
BP86G3 = Gibbs_step(step_3_BP86, BP86energy) - BP86G
BP86G4 = Gibbs_step(step_4_BP86, BP86energy) - BP86G
BP86G5 = Gibbs_step(step_5_BP86, BP86energy) - BP86G

#Find energy difference for each reaction step
BP86DG1 = round((BP86G2 - BP86G1),2)
BP86DG2 = round((BP86G3 - BP86G2),2)
BP86DG3 = round((BP86G4 - BP86G3),2)
BP86DG4 = round((BP86G5 - BP86G4),2)

######
#PBE0#
######
#Collect each step as a list of coefficients and the energies as a seperate list
step_1_PBE0 = pd.to_numeric(dfPBE0.iloc[0, :])
step_2_PBE0 = pd.to_numeric(dfPBE0.iloc[1, :])
step_3_PBE0 = pd.to_numeric(dfPBE0.iloc[2, :])
step_4_PBE0 = pd.to_numeric(dfPBE0.iloc[3, :])
step_5_PBE0 = pd.to_numeric(dfPBE0.iloc[4, :])
# PBE0energy = pd.to_numeric(dfPBE0.iloc[5, :])
PBE0energy = pd.to_numeric(dfPBE0.iloc[6, :])

#Find relative energy level for each reaction step
PBE0G = Gibbs_step(step_1_PBE0, PBE0energy)
PBE0G1 = (Gibbs_step(step_1_PBE0, PBE0energy)) - PBE0G
PBE0G2 = Gibbs_step(step_2_PBE0, PBE0energy) - PBE0G
PBE0G3 = Gibbs_step(step_3_PBE0, PBE0energy) - PBE0G
PBE0G4 = Gibbs_step(step_4_PBE0, PBE0energy) - PBE0G
PBE0G5 = Gibbs_step(step_5_PBE0, PBE0energy) - PBE0G

#Find energy difference for each reaction step
PBE0DG1 = round((PBE0G2 - PBE0G1),2)
PBE0DG2 = round((PBE0G3 - PBE0G2),2)
PBE0DG3 = round((PBE0G4 - PBE0G3),2)
PBE0DG4 = round((PBE0G5 - PBE0G4),2)

#######
#B3LYP#
#######
#Collect each step as a list of coefficients and the energies as a seperate list
step_1_B3LYP = pd.to_numeric(dfB3LYP.iloc[0, :])
step_2_B3LYP = pd.to_numeric(dfB3LYP.iloc[1, :])
step_3_B3LYP = pd.to_numeric(dfB3LYP.iloc[2, :])
step_4_B3LYP = pd.to_numeric(dfB3LYP.iloc[3, :])
step_5_B3LYP = pd.to_numeric(dfB3LYP.iloc[4, :])
# B3LYPenergy = pd.to_numeric(dfB3LYP.iloc[5, :])
B3LYPenergy = pd.to_numeric(dfB3LYP.iloc[6, :])

#Find relative energy level each reaction step
B3LYPG = Gibbs_step(step_1_B3LYP, B3LYPenergy)
B3LYPG1 = (Gibbs_step(step_1_B3LYP, B3LYPenergy)) - B3LYPG
B3LYPG2 = Gibbs_step(step_2_B3LYP, B3LYPenergy) - B3LYPG
B3LYPG3 = Gibbs_step(step_3_B3LYP, B3LYPenergy) - B3LYPG
B3LYPG4 = Gibbs_step(step_4_B3LYP, B3LYPenergy) - B3LYPG
B3LYPG5 = Gibbs_step(step_5_B3LYP, B3LYPenergy) - B3LYPG

#Find energy difference for each reaction step
B3LYPDG1 = round((B3LYPG2 - B3LYPG1),2)
B3LYPDG2 = round((B3LYPG3 - B3LYPG2),2)
B3LYPDG3 = round((B3LYPG4 - B3LYPG3),2)
B3LYPDG4 = round((B3LYPG5 - B3LYPG4),2)

########
#M06-2X#
########
#Collect each step as a list of coefficients and the energies as a seperate list
step_1_M062X = pd.to_numeric(dfM062X.iloc[0, :])
step_2_M062X = pd.to_numeric(dfM062X.iloc[1, :])
step_3_M062X = pd.to_numeric(dfM062X.iloc[2, :])
step_4_M062X = pd.to_numeric(dfM062X.iloc[3, :])
step_5_M062X = pd.to_numeric(dfM062X.iloc[4, :])
# M062Xenergy = pd.to_numeric(dfM062X.iloc[5, :])
M062Xenergy = pd.to_numeric(dfM062X.iloc[6, :])

#Find relative energy level for each reaction step
M062XG = Gibbs_step(step_1_M062X, M062Xenergy)
M062XG1 = (Gibbs_step(step_1_M062X, M062Xenergy)) - M062XG
M062XG2 = Gibbs_step(step_2_M062X, M062Xenergy) - M062XG
M062XG3 = Gibbs_step(step_3_M062X, M062Xenergy) - M062XG
M062XG4 = Gibbs_step(step_4_M062X, M062Xenergy) - M062XG
M062XG5 = Gibbs_step(step_5_M062X, M062Xenergy) - M062XG

#Find energy difference for each reaction step
M062XDG1 = round((M062XG2 - M062XG1),2)
M062XDG2 = round((M062XG3 - M062XG2),2)
M062XDG3 = round((M062XG4 - M062XG3),2)
M062XDG4 = round((M062XG5 - M062XG4),2)

########
#wB97XD#
########
#Collect each step as a list of coefficients and the energies as a seperate list
step_1_wB97XD = pd.to_numeric(dfwB97XD.iloc[0, :])
step_2_wB97XD = pd.to_numeric(dfwB97XD.iloc[1, :])
step_3_wB97XD = pd.to_numeric(dfwB97XD.iloc[2, :])
step_4_wB97XD = pd.to_numeric(dfwB97XD.iloc[3, :])
step_5_wB97XD = pd.to_numeric(dfwB97XD.iloc[4, :])
# wB97XDenergy = pd.to_numeric(dfwB97XD.iloc[5, :])
wB97XDenergy = pd.to_numeric(dfwB97XD.iloc[6, :])

#Find relative energy level for each reaction step
wB97XDG = Gibbs_step(step_1_wB97XD, wB97XDenergy)
wB97XDG1 = (Gibbs_step(step_1_wB97XD, wB97XDenergy)) - wB97XDG
wB97XDG2 = Gibbs_step(step_2_wB97XD, wB97XDenergy) - wB97XDG
wB97XDG3 = Gibbs_step(step_3_wB97XD, wB97XDenergy) - wB97XDG
wB97XDG4 = Gibbs_step(step_4_wB97XD, wB97XDenergy) - wB97XDG
wB97XDG5 = Gibbs_step(step_5_wB97XD, wB97XDenergy) - wB97XDG

#Find energy difference for each reaction step
wB97XDDG1 = round((wB97XDG2 - wB97XDG1),2)
wB97XDDG2 = round((wB97XDG3 - wB97XDG2),2)
wB97XDDG3 = round((wB97XDG4 - wB97XDG3),2)
wB97XDDG4 = round((wB97XDG5 - wB97XDG4),2)

#####
#M06#
#####
#Collect each step as a list of coefficients and the energies as a seperate list
step_1_M06 = pd.to_numeric(dfM06.iloc[0, :])
step_2_M06 = pd.to_numeric(dfM06.iloc[1, :])
step_3_M06 = pd.to_numeric(dfM06.iloc[2, :])
step_4_M06 = pd.to_numeric(dfM06.iloc[3, :])
step_5_M06 = pd.to_numeric(dfM06.iloc[4, :])
# M06energy = pd.to_numeric(dfM06.iloc[5, :])
M06energy = pd.to_numeric(dfM06.iloc[6, :])

#Find relative energy level for each reaction step
M06G = Gibbs_step(step_1_M06, M06energy)
M06G1 = (Gibbs_step(step_1_M06, M06energy)) - M06G
M06G2 = Gibbs_step(step_2_M06, M06energy) - M06G
M06G3 = Gibbs_step(step_3_M06, M06energy) - M06G
M06G4 = Gibbs_step(step_4_M06, M06energy) - M06G
M06G5 = Gibbs_step(step_5_M06, M06energy) - M06G

#Find energy difference for each reaction step
M06DG1 = round((M06G2 - M06G1),2)
M06DG2 = round((M06G3 - M06G2),2)
M06DG3 = round((M06G4 - M06G3),2)
M06DG4 = round((M06G5 - M06G4),2)

###############################################################################
#Plots
###############################################################################
#Define axes
xaxis = (1, 2, 3, 4, 5)
BP86yaxis = (BP86G1, BP86G2, BP86G3, BP86G4, BP86G5)
PBE0yaxis = (PBE0G1, PBE0G2, PBE0G3, PBE0G4, PBE0G5)
B3LYPyaxis = (B3LYPG1, B3LYPG2, B3LYPG3, B3LYPG4, B3LYPG5)
M062Xyaxis = (M062XG1, M062XG2, M062XG3, M062XG4, M062XG5)
wB97XDyaxis = (wB97XDG1, wB97XDG2, wB97XDG3, wB97XDG4, wB97XDG5)
M06yaxis = (M06G1, M06G2, M06G3, M06G4, M06G5)

#Plot figure
# mainplot = plt.figure(figsize=(10,10))
plt.rcParams["figure.figsize"] = [15, 10]
plt.rcParams["figure.autolayout"] = True
fig, ax1 = plt.subplots()


#Plot for each step's energy level
######
#BP86#
######
#Scatterplot
ax1.scatter(xaxis, BP86yaxis, s = 2000, c = "black", marker = "_", linewidths = 3)

#Energy change line
ax1.plot((1.11, 1.89), (0, BP86G2), c = "black", linestyle = "dashed")
ax1.plot((2.11, 2.89), (BP86G2, BP86G3), c = "black", linestyle = "dashed")
ax1.plot((3.11, 3.89), (BP86G3, BP86G4), c = "black", linestyle = "dashed")
ax1.plot((4.11, 4.89), (BP86G4, BP86G5), c = "black", linestyle = "dashed")

######
#PBE0#
######
#Scatterplot
ax1.scatter(xaxis, PBE0yaxis, s = 2000, c = "blue", marker = "_", linewidths = 3)

#Energy change line
ax1.plot((1.11, 1.89), (0, PBE0G2), c = "blue", linestyle = "dashed")
ax1.plot((2.11, 2.89), (PBE0G2, PBE0G3), c = "blue", linestyle = "dashed")
ax1.plot((3.11, 3.89), (PBE0G3, PBE0G4), c = "blue", linestyle = "dashed")
ax1.plot((4.11, 4.89), (PBE0G4, PBE0G5), c = "blue", linestyle = "dashed")

#######
#B3LYP#
#######
# Scatterplot
ax1.scatter(xaxis, B3LYPyaxis, s = 2000, c = "green", marker = "_", linewidths = 3)

#Energy change line
ax1.plot((1.11, 1.89), (0, B3LYPG2), c = "green", linestyle = "dashed")
ax1.plot((2.11, 2.89), (B3LYPG2, B3LYPG3), c = "green", linestyle = "dashed")
ax1.plot((3.11, 3.89), (B3LYPG3, B3LYPG4), c = "green", linestyle = "dashed")
ax1.plot((4.11, 4.89), (B3LYPG4, B3LYPG5), c = "green", linestyle = "dashed")

########
#M06-2X#
########
#Scatterplot
ax1.scatter(xaxis, M062Xyaxis, s = 2000, c = "pink", marker = "_", linewidths = 3)

#Energy change line
ax1.plot((1.11, 1.89), (0, M062XG2), c = "pink", linestyle = "dashed")
ax1.plot((2.11, 2.89), (M062XG2, M062XG3), c = "pink", linestyle = "dashed")
ax1.plot((3.11, 3.89), (M062XG3, M062XG4), c = "pink", linestyle = "dashed")
ax1.plot((4.11, 4.89), (M062XG4, M062XG5), c = "pink", linestyle = "dashed")

########
#wB97XD#
########
#Scatterplot
ax1.scatter(xaxis, wB97XDyaxis, s = 2000, c = "purple", marker = "_", linewidths = 3)

#Energy change line
ax1.plot((1.11, 1.89), (0, wB97XDG2), c = "purple", linestyle = "dashed")
ax1.plot((2.11, 2.89), (wB97XDG2, wB97XDG3), c = "purple", linestyle = "dashed")
ax1.plot((3.11, 3.89), (wB97XDG3, wB97XDG4), c = "purple", linestyle = "dashed")
ax1.plot((4.11, 4.89), (wB97XDG4, wB97XDG5), c = "purple", linestyle = "dashed")

#####
#M06#
#####
#Scatterplot
ax1.scatter(xaxis, M06yaxis, s = 2000, c = "orange", marker = "_", linewidths = 3)
ax1.set_ylabel("Gibbs free energy (kcal mol$^{-1}$)", fontsize = "18")

#Energy change line
ax1.plot((1.11, 1.89), (0, M06G2), c = "orange", linestyle = "dashed")
ax1.plot((2.11, 2.89), (M06G2, M06G3), c = "orange", linestyle = "dashed")
ax1.plot((3.11, 3.89), (M06G3, M06G4), c = "orange", linestyle = "dashed")
ax1.plot((4.11, 4.89), (M06G4, M06G5), c = "orange", linestyle = "dashed")

#Plot font
plt.rcParams['font.family'] = "serif"
plt.rcParams.update({'font.size': 18})

#Plot text boxes
ax1.text(1.11, -7, "Williamson Ether Synthesis", bbox = {'facecolor': "white", "pad": 4}, fontsize = 12)
ax1.text(2.24, -3, "Oxime formation", bbox = {'facecolor': "white", "pad": 4}, fontsize = 12)
ax1.text(3.07, -35, "Dehydration", bbox = {'facecolor': "white", "pad": 4}, fontsize = 12)
ax1.text(4.35, -75, "Hydrolysis", bbox = {'facecolor': "white", "pad": 4}, fontsize = 12)

#Plot subplot
ax2 = fig.add_axes([.1170, .08, .35, .35])
ax2.plot()

#Plot barcharts and x-axis line
ax2.plot((2,18), (0,0), color = "black", linewidth = 0.5)
x2 = np.arange(4, 17, 4)
y2BP86 = [BP86DG1, BP86DG2, BP86DG3, BP86DG4]
y2PBE0 = [PBE0DG1, PBE0DG2, PBE0DG3, PBE0DG4] 
y2B3LYP = [B3LYPDG1, B3LYPDG2, B3LYPDG3, B3LYPDG4]
y2M062X = [M062XDG1, M062XDG2, M062XDG3, M062XDG4]
y2wB97XD = [wB97XDDG1, wB97XDDG2, wB97XDDG3, wB97XDDG4]
y2M06 = [M06DG1, M06DG2, M06DG3, M06DG4]

ax2.plot((2,18), (10,10), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((2,18), (-10,-10), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((2,18), (-20,-20), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((2,18), (-30,-30), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((2,18), (-40,-40), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((2,18), (-50,-50), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((2,18), (-60,-60), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((2,18), (-70,-70), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((2,18), (-80,-80), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)

ax2.bar(x2 - 1.5, y2BP86, 0.5, color = "black")
ax2.bar(x2 - 1, y2PBE0, 0.5, color = "blue")
ax2.bar(x2 - 0.5, y2B3LYP, 0.5, color = "green")
ax2.bar(x2, y2M062X, 0.5, color = "pink")
ax2.bar(x2 + 0.5, y2wB97XD, 0.5, color = "purple")
ax2.bar(x2 + 1, y2M06, 0.5, color = "orange")

ax1.text(0.985, -41.67, "Stepwise ΔG", bbox = {'facecolor': "white", "pad": 4}, fontsize = 14)


#Ticks
ax1.set_xticks([])
ax2.set_xticks([])
ax1.set_yticks([10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50, -55, -60, -65, -70, -75, -80])
ax2.set_yticks([10, 0, -10, -20, -30, -40, -50, -60, -70, -80])
ax2.yaxis.tick_right()

#Limits
ax1.set_ylim([-85, 15])
ax2.set_xlim(2,18)
ax2.set_ylim([-70, 15])

#Colour parts of plots
ax1.fill_between((1, 2), -100, 15, facecolor = "green", alpha = 0.1)
ax1.fill_between((3, 4), -100, 15, facecolor = "blue", alpha = 0.1)
ax1.fill_between((4, 5), -100, 15, facecolor = "orange", alpha = 0.1)

ax2.fill_between((2, 5.75), -75, 15, facecolor = "green", alpha = 0.1)
ax2.fill_between((9.75, 13.75), -75, 15, facecolor = "blue", alpha = 0.1)
ax2.fill_between((13.75, 18), -75, 15, facecolor = "orange", alpha = 0.1)

#Legend
BP86leg = mlines.Line2D([], [], color = "black", linestyle = "dashed", label = "BP86")
PBE0leg = mlines.Line2D([], [], color = "blue", linestyle = "dashed", label = "PBE0")
B3LYPleg = mlines.Line2D([], [], color = "green", linestyle = "dashed", label = "B3LYP")
M062Xleg = mlines.Line2D([], [], color = "pink", linestyle = "dashed", label = "M06-2X")
wB97XDleg = mlines.Line2D([], [], color = "purple", linestyle = "dashed", label = "wB97XD")
M06leg = mlines.Line2D([], [], color = "orange", linestyle = "dashed", label = "M06")
legends = (BP86leg, PBE0leg, B3LYPleg, M062Xleg, wB97XDleg, M06leg)
ax1.legend(handles=legends, loc="upper right")

plt.savefig("All functional.png", format = "png", bbox_inches='tight', dpi = 300)
plt.show()
