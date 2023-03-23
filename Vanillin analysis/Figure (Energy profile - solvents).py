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
    
dfPBE0 = df.iloc[9:16, 1:15]
dfM06 = df.iloc[41:48, 1:15]
    
#Equation for element-wise multiplication (coefficient * energy of molecule)
def Gibbs_step(x, y):
    G = x*y
    return sum(G)


###########################################################################
#Databases
###########################################################################
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

#Find relative energy level each reaction step
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

PBE0GasG = PBE0G
PBE0GasG1 = PBE0G1
PBE0GasG2 = PBE0G2
PBE0GasG3 = PBE0G3
PBE0GasG4 = PBE0G4
PBE0GasG5 = PBE0G5

PBE0GasDG1 = PBE0DG1
PBE0GasDG2 = PBE0DG2
PBE0GasDG3 = PBE0DG3
PBE0GasDG4 = PBE0DG4

M06GasG = M06G
M06GasG1 = M06G1
M06GasG2 = M06G2
M06GasG3 = M06G3
M06GasG4 = M06G4
M06GasG5 = M06G5

M06GasDG1 = M06DG1
M06GasDG2 = M06DG2
M06GasDG3 = M06DG3
M06GasDG4 = M06DG4

sheet = ("Gibbs (Water) (SMD)", "Gibbs (Ethanol) (SMD)", "Gibbs (Acetonitrile) (SMD)")
for i in sheet:

    df = pd.read_excel("Z:/Michael Nicolaou/Projects/Vanillin-veratric acid/Workbench.xlsx", sheet_name=i, index_col="Functional")
    
    dfPBE0 = df.iloc[9:16, 1:15]
    dfM06 = df.iloc[41:48, 1:15]
    
    #Equation for element-wise multiplication (coefficient * energy of molecule)
    def Gibbs_step(x, y):
        G = x*y
        return sum(G)
    
    
    ###########################################################################
    #Databases
    ###########################################################################
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
    PBE0G1 = (Gibbs_step(step_1_PBE0, PBE0energy)) - PBE0GasG
    PBE0G2 = Gibbs_step(step_2_PBE0, PBE0energy) - PBE0GasG
    PBE0G3 = Gibbs_step(step_3_PBE0, PBE0energy) - PBE0GasG
    PBE0G4 = Gibbs_step(step_4_PBE0, PBE0energy) - PBE0GasG
    PBE0G5 = Gibbs_step(step_5_PBE0, PBE0energy) - PBE0GasG
    
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
    
    #Find relative energy level each reaction step
    M06G1 = (Gibbs_step(step_1_M06, M06energy)) - M06GasG
    M06G2 = Gibbs_step(step_2_M06, M06energy) - M06GasG
    M06G3 = Gibbs_step(step_3_M06, M06energy) - M06GasG
    M06G4 = Gibbs_step(step_4_M06, M06energy) - M06GasG
    M06G5 = Gibbs_step(step_5_M06, M06energy) - M06GasG
    
    #Find energy difference for each reaction step
    M06DG1 = round((M06G2 - M06G1),2)
    M06DG2 = round((M06G3 - M06G2),2)
    M06DG3 = round((M06G4 - M06G3),2)
    M06DG4 = round((M06G5 - M06G4),2)

    if i == "Gibbs (Water) (SMD)":
        PBE0WaterG1 = PBE0G1
        PBE0WaterG2 = PBE0G2
        PBE0WaterG3 = PBE0G3
        PBE0WaterG4 = PBE0G4
        PBE0WaterG5 = PBE0G5
        
        PBE0WaterDG1 = PBE0DG1
        PBE0WaterDG2 = PBE0DG2
        PBE0WaterDG3 = PBE0DG3
        PBE0WaterDG4 = PBE0DG4
        
        M06WaterG1 = M06G1
        M06WaterG2 = M06G2
        M06WaterG3 = M06G3
        M06WaterG4 = M06G4
        M06WaterG5 = M06G5
        
        M06WaterDG1 = M06DG1
        M06WaterDG2 = M06DG2
        M06WaterDG3 = M06DG3
        M06WaterDG4 = M06DG4
        
    elif i == "Gibbs (Ethanol) (SMD)":
        PBE0EthanolG1 = PBE0G1
        PBE0EthanolG2 = PBE0G2
        PBE0EthanolG3 = PBE0G3
        PBE0EthanolG4 = PBE0G4
        PBE0EthanolG5 = PBE0G5
        
        PBE0EthanolDG1 = PBE0DG1
        PBE0EthanolDG2 = PBE0DG2
        PBE0EthanolDG3 = PBE0DG3
        PBE0EthanolDG4 = PBE0DG4
        
        M06EthanolG1 = M06G1
        M06EthanolG2 = M06G2
        M06EthanolG3 = M06G3
        M06EthanolG4 = M06G4
        M06EthanolG5 = M06G5
        
        M06EthanolDG1 = M06DG1
        M06EthanolDG2 = M06DG2
        M06EthanolDG3 = M06DG3
        M06EthanolDG4 = M06DG4
    
    elif i == "Gibbs (Acetonitrile) (SMD)":
        PBE0AcetonitrileG1 = PBE0G1
        PBE0AcetonitrileG2 = PBE0G2
        PBE0AcetonitrileG3 = PBE0G3
        PBE0AcetonitrileG4 = PBE0G4
        PBE0AcetonitrileG5 = PBE0G5
        
        PBE0AcetonitrileDG1 = PBE0DG1
        PBE0AcetonitrileDG2 = PBE0DG2
        PBE0AcetonitrileDG3 = PBE0DG3
        PBE0AcetonitrileDG4 = PBE0DG4
        
        M06AcetonitrileG1 = M06G1
        M06AcetonitrileG2 = M06G2
        M06AcetonitrileG3 = M06G3
        M06AcetonitrileG4 = M06G4
        M06AcetonitrileG5 = M06G5
        
        M06AcetonitrileDG1 = M06DG1
        M06AcetonitrileDG2 = M06DG2
        M06AcetonitrileDG3 = M06DG3
        M06AcetonitrileDG4 = M06DG4
        
###############################################################################
#Plots
###############################################################################
#Define axes
xaxis = (1, 2, 3, 4, 5)
PBE0Gasyaxis = (PBE0GasG1, PBE0GasG2, PBE0GasG3, PBE0GasG4, PBE0GasG5)
PBE0Wateryaxis = (PBE0WaterG1, PBE0WaterG2, PBE0WaterG3, PBE0WaterG4, PBE0WaterG5)
PBE0Ethanolyaxis = (PBE0EthanolG1, PBE0EthanolG2, PBE0EthanolG3, PBE0EthanolG4, PBE0EthanolG5)
PBE0Acetonitrileyaxis = (PBE0AcetonitrileG1, PBE0AcetonitrileG2, PBE0AcetonitrileG3, PBE0AcetonitrileG4, PBE0AcetonitrileG5)
M06Gasyaxis = (M06GasG1, M06GasG2, M06GasG3, M06GasG4, M06GasG5)
M06Wateryaxis = (M06WaterG1, M06WaterG2, M06WaterG3, M06WaterG4, M06WaterG5)
M06Ethanolyaxis = (M06EthanolG1, M06EthanolG2, M06EthanolG3, M06EthanolG4, M06EthanolG5)
M06Acetonitrileyaxis = (M06AcetonitrileG1, M06AcetonitrileG2, M06AcetonitrileG3, M06AcetonitrileG4, M06AcetonitrileG5)

#Plot figure
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
# plt.subplots_adjust(bottom = -0.2, left = 0, top = 1., right = 1)
sub1 = fig.add_subplot(2, 2, (1,2))
sub2 = fig.add_subplot(2, 2, (3,4))

#Plot for each step's energy level
######
#BP86#
######
#Scatterplot
sub1.scatter(xaxis, PBE0Gasyaxis, s = 2000, c = "blue", marker = "_", linewidths = 3)
sub1.scatter(xaxis, PBE0Wateryaxis, s = 2000, c = "cyan", marker = "_", linewidths = 3)
sub1.scatter(xaxis, PBE0Ethanolyaxis, s = 2000, c = "navy", marker = "_", linewidths = 3)
sub1.scatter(xaxis, PBE0Acetonitrileyaxis, s = 2000, c = "cornflowerblue", marker = "_", linewidths = 3)

sub2.scatter(xaxis, M06Gasyaxis, s = 2000, c = "orange", marker = "_", linewidths = 3)
sub2.scatter(xaxis, M06Wateryaxis, s = 2000, c = "red", marker = "_", linewidths = 3)
sub2.scatter(xaxis, M06Ethanolyaxis, s = 2000, c = "goldenrod", marker = "_", linewidths = 3)
sub2.scatter(xaxis, M06Acetonitrileyaxis, s = 2000, c = "salmon", marker = "_", linewidths = 3)

#Energy change line
sub1.plot((1.08, 1.92), (PBE0GasG1, PBE0GasG2), c = "blue", linestyle = "dashed")
sub1.plot((2.08, 2.92), (PBE0GasG2, PBE0GasG3), c = "blue", linestyle = "dashed")
sub1.plot((3.08, 3.92), (PBE0GasG3, PBE0GasG4), c = "blue", linestyle = "dashed")
sub1.plot((4.08, 4.92), (PBE0GasG4, PBE0GasG5), c = "blue", linestyle = "dashed")

sub1.plot((1.08, 1.92), (PBE0WaterG1, PBE0WaterG2), c = "cyan", linestyle = "dashed")
sub1.plot((2.08, 2.92), (PBE0WaterG2, PBE0WaterG3), c = "cyan", linestyle = "dashed")
sub1.plot((3.08, 3.92), (PBE0WaterG3, PBE0WaterG4), c = "cyan", linestyle = "dashed")
sub1.plot((4.08, 4.92), (PBE0WaterG4, PBE0WaterG5), c = "cyan", linestyle = "dashed")

sub1.plot((1.08, 1.92), (PBE0EthanolG1, PBE0EthanolG2), c = "navy", linestyle = "dashed")
sub1.plot((2.08, 2.92), (PBE0EthanolG2, PBE0EthanolG3), c = "navy", linestyle = "dashed")
sub1.plot((3.08, 3.92), (PBE0EthanolG3, PBE0EthanolG4), c = "navy", linestyle = "dashed")
sub1.plot((4.08, 4.92), (PBE0EthanolG4, PBE0EthanolG5), c = "navy", linestyle = "dashed")

sub1.plot((1.08, 1.92), (PBE0AcetonitrileG1, PBE0AcetonitrileG2), c = "cornflowerblue", linestyle = "dashed")
sub1.plot((2.08, 2.92), (PBE0AcetonitrileG2, PBE0AcetonitrileG3), c = "cornflowerblue", linestyle = "dashed")
sub1.plot((3.08, 3.92), (PBE0AcetonitrileG3, PBE0AcetonitrileG4), c = "cornflowerblue", linestyle = "dashed")
sub1.plot((4.08, 4.92), (PBE0AcetonitrileG4, PBE0AcetonitrileG5), c = "cornflowerblue", linestyle = "dashed")

sub2.plot((1.08, 1.92), (M06GasG1, M06GasG2), c = "orange", linestyle = "dashed")
sub2.plot((2.08, 2.92), (M06GasG2, M06GasG3), c = "orange", linestyle = "dashed")
sub2.plot((3.08, 3.92), (M06GasG3, M06GasG4), c = "orange", linestyle = "dashed")
sub2.plot((4.08, 4.92), (M06GasG4, M06GasG5), c = "orange", linestyle = "dashed")

sub2.plot((1.08, 1.92), (M06WaterG1, M06WaterG2), c = "red", linestyle = "dashed")
sub2.plot((2.08, 2.92), (M06WaterG2, M06WaterG3), c = "red", linestyle = "dashed")
sub2.plot((3.08, 3.92), (M06WaterG3, M06WaterG4), c = "red", linestyle = "dashed")
sub2.plot((4.08, 4.92), (M06WaterG4, M06WaterG5), c = "red", linestyle = "dashed")

sub2.plot((1.08, 1.92), (M06EthanolG1, M06EthanolG2), c = "goldenrod", linestyle = "dashed")
sub2.plot((2.08, 2.92), (M06EthanolG2, M06EthanolG3), c = "goldenrod", linestyle = "dashed")
sub2.plot((3.08, 3.92), (M06EthanolG3, M06EthanolG4), c = "goldenrod", linestyle = "dashed")
sub2.plot((4.08, 4.92), (M06EthanolG4, M06EthanolG5), c = "goldenrod", linestyle = "dashed")

sub2.plot((1.08, 1.92), (M06AcetonitrileG1, M06AcetonitrileG2), c = "salmon", linestyle = "dashed")
sub2.plot((2.08, 2.92), (M06AcetonitrileG2, M06AcetonitrileG3), c = "salmon", linestyle = "dashed")
sub2.plot((3.08, 3.92), (M06AcetonitrileG3, M06AcetonitrileG4), c = "salmon", linestyle = "dashed")
sub2.plot((4.08, 4.92), (M06AcetonitrileG4, M06AcetonitrileG5), c = "salmon", linestyle = "dashed")

#Plot font
plt.rcParams['font.family'] = "serif"
plt.rcParams.update({'font.size': 18})

#Axis labels
sub1.set_ylabel("Gibbs free energy (kcal mol$^{-1}$)", fontsize = 12)
sub2.set_ylabel("Gibbs free energy (kcal mol$^{-1}$)", fontsize = 12)

#Limits
sub1.set_ylim([-130, 15])
sub2.set_ylim([-130, 15])

#Ticks
sub1.set_xticks([])
sub2.set_xticks([])
sub1.set_yticks([10, 0, -10, -20, -30, -40, -50, -60, -70 , -80, -90, -100, -110, -120, -130])
sub2.set_yticks([10, 0, -10, -20, -30, -40, -50, -60, -70 , -80, -90, -100, -110, -120, -130])

#Plot titles
sub1.text(0.84, -123, "PBE0", bbox = {'facecolor': "white", "pad": 4}, fontsize = 20)
sub2.text(0.84, -123, "M06", bbox = {'facecolor': "white", "pad": 4}, fontsize = 20)

#Colour parts of plots
sub1.fill_between((1, 2), -130, 15, facecolor = "green", alpha = 0.1)
sub1.fill_between((3, 4), -130, 15, facecolor = "blue", alpha = 0.1)
sub1.fill_between((4, 5), -130, 15, facecolor = "orange", alpha = 0.1)

sub2.fill_between((1, 2), -130, 15, facecolor = "green", alpha = 0.1)
sub2.fill_between((3, 4), -130, 15, facecolor = "blue", alpha = 0.1)
sub2.fill_between((4, 5), -130, 15, facecolor = "orange", alpha = 0.1)

#Legend
PBE0Gasleg = mlines.Line2D([], [], color = "blue", linestyle = "dashed", label = "Gas")
PBE0Waterleg = mlines.Line2D([], [], color = "cyan", linestyle = "dashed", label = "Water")
PBE0Ethanolleg = mlines.Line2D([], [], color = "navy", linestyle = "dashed", label = "Ethanol")
PBE0Acetonitrileleg = mlines.Line2D([], [], color = "cornflowerblue", linestyle = "dashed", label = "Acetonitrile")
M06Gasleg = mlines.Line2D([], [], color = "orange", linestyle = "dashed", label = "Gas")
M06Waterleg = mlines.Line2D([], [], color = "red", linestyle = "dashed", label = "Water")
M06Ethanolleg = mlines.Line2D([], [], color = "goldenrod", linestyle = "dashed", label = "Ethanol")
M06Acetonitrileleg = mlines.Line2D([], [], color = "salmon", linestyle = "dashed", label = "Acetonitrile")
PBE0legends = (PBE0Gasleg, PBE0Waterleg, PBE0Ethanolleg, PBE0Acetonitrileleg)
M06legends = (M06Gasleg, M06Waterleg, M06Ethanolleg, M06Acetonitrileleg)
sub1.legend(handles=PBE0legends, loc="upper right")
sub2.legend(handles=M06legends, loc="upper right")

plt.savefig("All solvents.png", format = "png", bbox_inches='tight', dpi = 300)
plt.show()
