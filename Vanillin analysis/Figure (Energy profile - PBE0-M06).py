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
dfPBE0 = df.iloc[9:16, 1:15]
dfM06 = df.iloc[41:48, 1:15]

#Equation for element-wise multiplication (coefficient * energy of molecule)
def Gibbs_step(x, y):
    G = x*y
    return sum(G)


################################################################################
#Databases
################################################################################
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
PBE0yaxis = (PBE0G1, PBE0G2, PBE0G3, PBE0G4, PBE0G5)
M06yaxis = (M06G1, M06G2, M06G3, M06G4, M06G5)

#Plot figure
# mainplot = plt.figure(figsize=(10,10))
plt.rcParams["figure.figsize"] = [15, 10]
plt.rcParams["figure.autolayout"] = True
fig, ax1 = plt.subplots()


#Plot for each step's energy level
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
ax2.plot((-0.25, 7.75), (0,0), color = "black", linewidth = 0.5)
x2 = np.arange(1, 9, 2)
y2PBE0 = [PBE0DG1, PBE0DG2, PBE0DG3, PBE0DG4] 
y2M06 = [M06DG1, M06DG2, M06DG3, M06DG4]

ax2.plot((-0.25, 7.75), (10,10), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((-0.25, 7.75), (-10,-10), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((-0.25, 7.75), (-20,-20), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((-0.25, 7.75), (-30,-30), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((-0.25, 7.75), (-40,-40), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((-0.25, 7.75), (-50,-50), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((-0.25, 7.75), (-60,-60), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((-0.25, 7.75), (-70,-70), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)
ax2.plot((-0.25, 7.75), (-80,-80), color = "black", linewidth = 0.7, alpha = 0.7, linestyle = "--", zorder = 1)

ax2.bar(x2 - 0.5, y2PBE0, 0.5, color = "blue")
ax2.bar(x2, y2M06, 0.5, color = "orange")

ax1.text(0.985, -41.67, "Stepwise ΔG", bbox = {'facecolor': "white", "pad": 4}, fontsize = 14)

#Scatter labels
ax1.text(1.96, (float(PBE0G2)-2.2), round(float(PBE0G2),1), color = "blue", fontsize = 12)
ax1.text(2.96, (float(PBE0G3)-2.2), round(float(PBE0G3),1), color = "blue", fontsize = 12)
ax1.text(3.93, (float(PBE0G4)-2.2), round(float(PBE0G4),1), color = "blue", fontsize = 12)
ax1.text(4.93, (float(PBE0G5)-2.2), round(float(PBE0G5),1), color = "blue", fontsize = 12)

ax1.text(1.96, (float(M06G2)+0.6), round(float(M06G2),1), color = "orange", fontsize = 12)
ax1.text(2.96, (float(M06G3)+0.6), round(float(M06G3),1), color = "orange", fontsize = 12)
ax1.text(3.93, (float(M06G4)+0.6), round(float(M06G4),1), color = "orange", fontsize = 12)
ax1.text(4.93, (float(M06G5)+0.6), round(float(M06G5),1), color = "orange", fontsize = 12)

#Ticks
ax1.set_xticks([])
ax2.set_xticks([])
ax1.set_yticks([10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50, -55, -60, -65, -70, -75, -80])
ax2.set_yticks([10, 0, -10, -20, -30, -40, -50, -60, -70, -80])
ax2.yaxis.tick_right()

#Limits
ax1.set_ylim([-85, 15])
ax2.set_xlim(-0.25, 7.75)
ax2.set_ylim([-70, 15])

#Colour parts of plots
ax1.fill_between((1, 2), -100, 15, facecolor = "green", alpha = 0.1)
ax1.fill_between((3, 4), -100, 15, facecolor = "blue", alpha = 0.1)
ax1.fill_between((4, 5), -100, 15, facecolor = "orange", alpha = 0.1)

ax2.fill_between((-0.25, 1.75), -70, 15, facecolor = "green", alpha = 0.1)
ax2.fill_between((3.75, 5.75), -70, 15, facecolor = "blue", alpha = 0.1)
ax2.fill_between((5.75, 8), -70, 15, facecolor = "orange", alpha = 0.1)

#Legend
PBE0leg = mlines.Line2D([], [], color = "blue", linestyle = "dashed", label = "PBE0")
M06leg = mlines.Line2D([], [], color = "orange", linestyle = "dashed", label = "M06")
legends = (PBE0leg, M06leg)
ax1.legend(handles=legends, loc="upper right")

plt.savefig("PBE0-M06.png", format = "png", bbox_inches='tight', dpi = 300)
plt.show()
