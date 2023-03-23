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
sheet = ("Gibbs (Water) (SMD)", "Gibbs (Ethanol) (SMD)", "Gibbs (Acetonitrile) (SMD)")
for i in sheet:

    df = pd.read_excel("Vanillin Data.xlsx", sheet_name=i, index_col="Functional")
    
    dfPBE0 = df.iloc[9:16, 1:15]
    
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

    if i == "Gibbs (Water) (SMD)":
        PBE0WaterG = PBE0G
        PBE0WaterG1 = PBE0G1
        PBE0WaterG2 = PBE0G2
        PBE0WaterG3 = PBE0G3
        PBE0WaterG4 = PBE0G4
        PBE0WaterG5 = PBE0G5
        
        PBE0WaterDG1 = PBE0DG1
        PBE0WaterDG2 = PBE0DG2
        PBE0WaterDG3 = PBE0DG3
        PBE0WaterDG4 = PBE0DG4
        
    elif i == "Gibbs (Ethanol) (SMD)":
        PBE0EthanolG = PBE0G
        PBE0EthanolG1 = PBE0G1
        PBE0EthanolG2 = PBE0G2
        PBE0EthanolG3 = PBE0G3
        PBE0EthanolG4 = PBE0G4
        PBE0EthanolG5 = PBE0G5
        
        PBE0EthanolDG1 = PBE0DG1
        PBE0EthanolDG2 = PBE0DG2
        PBE0EthanolDG3 = PBE0DG3
        PBE0EthanolDG4 = PBE0DG4

    elif i == "Gibbs (Acetonitrile) (SMD)":
        PBE0AcetonitrileG = PBE0G
        PBE0AcetonitrileG1 = PBE0G1
        PBE0AcetonitrileG2 = PBE0G2
        PBE0AcetonitrileG3 = PBE0G3
        PBE0AcetonitrileG4 = PBE0G4
        PBE0AcetonitrileG5 = PBE0G5
        
        PBE0AcetonitrileDG1 = PBE0DG1
        PBE0AcetonitrileDG2 = PBE0DG2
        PBE0AcetonitrileDG3 = PBE0DG3
        PBE0AcetonitrileDG4 = PBE0DG4

sheet = ("Gibbs (Water)", "Gibbs (Ethanol)", "Gibbs (Acetonitrile)")
for i in sheet:

    df = pd.read_excel("Z:/Michael Nicolaou/Projects/Vanillin-veratric acid/Workbench.xlsx", sheet_name=i, index_col="Functional")
    
    dfPBE0 = df.iloc[9:16, 1:15]
    
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
    if i == "Gibbs (Water)":
        PBE0G = Gibbs_step(step_1_PBE0, PBE0energy)
        PBE0G1 = (Gibbs_step(step_1_PBE0, PBE0energy)) - PBE0WaterG
        PBE0G2 = Gibbs_step(step_2_PBE0, PBE0energy) - PBE0WaterG
        PBE0G3 = Gibbs_step(step_3_PBE0, PBE0energy) - PBE0WaterG
        PBE0G4 = Gibbs_step(step_4_PBE0, PBE0energy) - PBE0WaterG
        PBE0G5 = Gibbs_step(step_5_PBE0, PBE0energy) - PBE0WaterG
    elif i == "Gibbs (Ethanol)":
        PBE0G = Gibbs_step(step_1_PBE0, PBE0energy)
        PBE0G1 = (Gibbs_step(step_1_PBE0, PBE0energy)) - PBE0EthanolG
        PBE0G2 = Gibbs_step(step_2_PBE0, PBE0energy) - PBE0EthanolG
        PBE0G3 = Gibbs_step(step_3_PBE0, PBE0energy) - PBE0EthanolG
        PBE0G4 = Gibbs_step(step_4_PBE0, PBE0energy) - PBE0EthanolG
        PBE0G5 = Gibbs_step(step_5_PBE0, PBE0energy) - PBE0EthanolG  
    elif i == "Gibbs (Acetonitrile)":
        PBE0G = Gibbs_step(step_1_PBE0, PBE0energy)
        PBE0G1 = (Gibbs_step(step_1_PBE0, PBE0energy)) - PBE0AcetonitrileG
        PBE0G2 = Gibbs_step(step_2_PBE0, PBE0energy) - PBE0AcetonitrileG
        PBE0G3 = Gibbs_step(step_3_PBE0, PBE0energy) - PBE0AcetonitrileG
        PBE0G4 = Gibbs_step(step_4_PBE0, PBE0energy) - PBE0AcetonitrileG
        PBE0G5 = Gibbs_step(step_5_PBE0, PBE0energy) - PBE0AcetonitrileG
        
    #Find energy difference for each reaction step
    PBE0DG1 = round((PBE0G2 - PBE0G1),2)
    PBE0DG2 = round((PBE0G3 - PBE0G2),2)
    PBE0DG3 = round((PBE0G4 - PBE0G3),2)
    PBE0DG4 = round((PBE0G5 - PBE0G4),2)

    if i == "Gibbs (Water)":
        PBE0WaterPCMG1 = PBE0G1
        PBE0WaterPCMG2 = PBE0G2
        PBE0WaterPCMG3 = PBE0G3
        PBE0WaterPCMG4 = PBE0G4
        PBE0WaterPCMG5 = PBE0G5
       
        PBE0WaterPCMDG1 = PBE0DG1
        PBE0WaterPCMDG2 = PBE0DG2
        PBE0WaterPCMDG3 = PBE0DG3
        PBE0WaterPCMDG4 = PBE0DG4

    elif i == "Gibbs (Ethanol)":
        PBE0EthanolPCMG1 = PBE0G1
        PBE0EthanolPCMG2 = PBE0G2
        PBE0EthanolPCMG3 = PBE0G3
        PBE0EthanolPCMG4 = PBE0G4
        PBE0EthanolPCMG5 = PBE0G5
        
        PBE0EthanolPCMDG1 = PBE0DG1
        PBE0EthanolPCMDG2 = PBE0DG2
        PBE0EthanolPCMDG3 = PBE0DG3
        PBE0EthanolPCMDG4 = PBE0DG4

    elif i == "Gibbs (Acetonitrile)":
        PBE0AcetonitrilePCMG1 = PBE0G1
        PBE0AcetonitrilePCMG2 = PBE0G2
        PBE0AcetonitrilePCMG3 = PBE0G3
        PBE0AcetonitrilePCMG4 = PBE0G4
        PBE0AcetonitrilePCMG5 = PBE0G5
        
        PBE0AcetonitrilePCMDG1 = PBE0DG1
        PBE0AcetonitrilePCMDG2 = PBE0DG2
        PBE0AcetonitrilePCMDG3 = PBE0DG3
        PBE0AcetonitrilePCMDG4 = PBE0DG4
        
###############################################################################
#Plots
###############################################################################
#Define axes
xaxis = (1, 2, 3, 4, 5)
PBE0Wateryaxis = (PBE0WaterG1, PBE0WaterG2, PBE0WaterG3, PBE0WaterG4, PBE0WaterG5)
PBE0Ethanolyaxis = (PBE0EthanolG1, PBE0EthanolG2, PBE0EthanolG3, PBE0EthanolG4, PBE0EthanolG5)
PBE0Acetonitrileyaxis = (PBE0AcetonitrileG1, PBE0AcetonitrileG2, PBE0AcetonitrileG3, PBE0AcetonitrileG4, PBE0AcetonitrileG5)
PBE0WaterPCMyaxis = (PBE0WaterPCMG1, PBE0WaterPCMG2, PBE0WaterPCMG3, PBE0WaterPCMG4, PBE0WaterPCMG5)
PBE0EthanolPCMyaxis = (PBE0EthanolPCMG1, PBE0EthanolPCMG2, PBE0EthanolPCMG3, PBE0EthanolPCMG4, PBE0EthanolPCMG5)
PBE0AcetonitrilePCMyaxis = (PBE0AcetonitrilePCMG1, PBE0AcetonitrilePCMG2, PBE0AcetonitrilePCMG3, PBE0AcetonitrilePCMG4, PBE0AcetonitrilePCMG5)


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
sub1 = fig.add_subplot(3, 3, (1, 3))
sub2 = fig.add_subplot(3, 3, (4, 6))
sub3 = fig.add_subplot(3, 3, (7, 9))

#Plot for each step's energy level
######
#BP86#
######
#Scatterplot
sub1.scatter(xaxis, PBE0Wateryaxis, s = 2000, c = "blue", marker = "_", linewidths = 3)
sub1.scatter(xaxis, PBE0WaterPCMyaxis, s = 2000, c = "cyan", marker = "_", linewidths = 3)

sub2.scatter(xaxis, PBE0Ethanolyaxis, s = 2000, c = "blue", marker = "_", linewidths = 3)
sub2.scatter(xaxis, PBE0EthanolPCMyaxis, s = 2000, c = "cyan", marker = "_", linewidths = 3)

sub3.scatter(xaxis, PBE0Acetonitrileyaxis, s = 2000, c = "blue", marker = "_", linewidths = 3)
sub3.scatter(xaxis, PBE0AcetonitrilePCMyaxis, s = 2000, c = "cyan", marker = "_", linewidths = 3)

#Energy change line
sub1.plot((1.08, 1.92), (PBE0WaterG1, PBE0WaterG2), c = "blue", linestyle = "dashed")
sub1.plot((2.08, 2.92), (PBE0WaterG2, PBE0WaterG3), c = "blue", linestyle = "dashed")
sub1.plot((3.08, 3.92), (PBE0WaterG3, PBE0WaterG4), c = "blue", linestyle = "dashed")
sub1.plot((4.08, 4.92), (PBE0WaterG4, PBE0WaterG5), c = "blue", linestyle = "dashed")

sub1.plot((1.08, 1.92), (PBE0WaterPCMG1, PBE0WaterPCMG2), c = "cyan", linestyle = "dashed")
sub1.plot((2.08, 2.92), (PBE0WaterPCMG2, PBE0WaterPCMG3), c = "cyan", linestyle = "dashed")
sub1.plot((3.08, 3.92), (PBE0WaterPCMG3, PBE0WaterPCMG4), c = "cyan", linestyle = "dashed")
sub1.plot((4.08, 4.92), (PBE0WaterPCMG4, PBE0WaterPCMG5), c = "cyan", linestyle = "dashed")

sub2.plot((1.08, 1.92), (PBE0EthanolG1, PBE0EthanolG2), c = "blue", linestyle = "dashed")
sub2.plot((2.08, 2.92), (PBE0EthanolG2, PBE0EthanolG3), c = "blue", linestyle = "dashed")
sub2.plot((3.08, 3.92), (PBE0EthanolG3, PBE0EthanolG4), c = "blue", linestyle = "dashed")
sub2.plot((4.08, 4.92), (PBE0EthanolG4, PBE0EthanolG5), c = "blue", linestyle = "dashed")

sub2.plot((1.08, 1.92), (PBE0EthanolPCMG1, PBE0EthanolPCMG2), c = "cyan", linestyle = "dashed")
sub2.plot((2.08, 2.92), (PBE0EthanolPCMG2, PBE0EthanolPCMG3), c = "cyan", linestyle = "dashed")
sub2.plot((3.08, 3.92), (PBE0EthanolPCMG3, PBE0EthanolPCMG4), c = "cyan", linestyle = "dashed")
sub2.plot((4.08, 4.92), (PBE0EthanolPCMG4, PBE0EthanolPCMG5), c = "cyan", linestyle = "dashed")

sub3.plot((1.08, 1.92), (PBE0AcetonitrileG1, PBE0AcetonitrileG2), c = "blue", linestyle = "dashed")
sub3.plot((2.08, 2.92), (PBE0AcetonitrileG2, PBE0AcetonitrileG3), c = "blue", linestyle = "dashed")
sub3.plot((3.08, 3.92), (PBE0AcetonitrileG3, PBE0AcetonitrileG4), c = "blue", linestyle = "dashed")
sub3.plot((4.08, 4.92), (PBE0AcetonitrileG4, PBE0AcetonitrileG5), c = "blue", linestyle = "dashed")

sub3.plot((1.08, 1.92), (PBE0AcetonitrilePCMG1, PBE0AcetonitrilePCMG2), c = "cyan", linestyle = "dashed")
sub3.plot((2.08, 2.92), (PBE0AcetonitrilePCMG2, PBE0AcetonitrilePCMG3), c = "cyan", linestyle = "dashed")
sub3.plot((3.08, 3.92), (PBE0AcetonitrilePCMG3, PBE0AcetonitrilePCMG4), c = "cyan", linestyle = "dashed")
sub3.plot((4.08, 4.92), (PBE0AcetonitrilePCMG4, PBE0AcetonitrilePCMG5), c = "cyan", linestyle = "dashed")

#Plot font
plt.rcParams['font.family'] = "serif"
plt.rcParams.update({'font.size': 18})

#Axis labels
sub1.set_ylabel("Gibbs free energy (kcal mol$^{-1}$)", fontsize = 12)
sub2.set_ylabel("Gibbs free energy (kcal mol$^{-1}$)", fontsize = 12)
sub3.set_ylabel("Gibbs free energy (kcal mol$^{-1}$)", fontsize = 12)

#Scatter labels
sub1.text(0.95, (float(PBE0WaterPCMG1)+3), round(float(PBE0WaterPCMG1),1), color = "cyan", fontsize = 12)
sub1.text(1.945, (float(PBE0WaterPCMG2)+3), round(float(PBE0WaterPCMG2),1), color = "cyan", fontsize = 12)
sub1.text(2.965, (float(PBE0WaterPCMG3)+3), round(float(PBE0WaterPCMG3),1), color = "cyan", fontsize = 12)
sub1.text(3.94, (float(PBE0WaterPCMG4)+3), round(float(PBE0WaterPCMG4),1), color = "cyan", fontsize = 12)
sub1.text(4.94, (float(PBE0WaterPCMG5)+3), round(float(PBE0WaterPCMG5),1), color = "cyan", fontsize = 12)

sub1.text(0.96, (float(PBE0WaterG1)-9.5), round(float(PBE0WaterG1),1), color = "blue", fontsize = 12)
sub1.text(1.96, (float(PBE0WaterG2)-9.5), round(float(PBE0WaterG2),1), color = "blue", fontsize = 12)
sub1.text(2.95, (float(PBE0WaterG3)-9.5), round(float(PBE0WaterG3),1), color = "blue", fontsize = 12)
sub1.text(3.94, (float(PBE0WaterG4)-9.5), round(float(PBE0WaterG4),1), color = "blue", fontsize = 12)
sub1.text(4.94, (float(PBE0WaterG5)-9.5), round(float(PBE0WaterG5),1), color = "blue", fontsize = 12)

sub2.text(0.95, (float(PBE0EthanolPCMG1)+3), round(float(PBE0EthanolPCMG1),1), color = "cyan", fontsize = 12)
sub2.text(1.945, (float(PBE0EthanolPCMG2)+3), round(float(PBE0EthanolPCMG2),1), color = "cyan", fontsize = 12)
sub2.text(2.945, (float(PBE0EthanolPCMG3)+3), round(float(PBE0EthanolPCMG3),1), color = "cyan", fontsize = 12)
sub2.text(3.94, (float(PBE0EthanolPCMG4)+3), round(float(PBE0EthanolPCMG4),1), color = "cyan", fontsize = 12)
sub2.text(4.94, (float(PBE0EthanolPCMG5)+3), round(float(PBE0EthanolPCMG5),1), color = "cyan", fontsize = 12)

sub2.text(0.96, (float(PBE0EthanolG1)-9.5), round(float(PBE0EthanolG1),1), color = "blue", fontsize = 12)
sub2.text(1.96, (float(PBE0EthanolG2)-9.5), round(float(PBE0EthanolG2),1), color = "blue", fontsize = 12)
sub2.text(2.95, (float(PBE0EthanolG3)-9.5), round(float(PBE0EthanolG3),1), color = "blue", fontsize = 12)
sub2.text(3.94, (float(PBE0EthanolG4)-9.5), round(float(PBE0EthanolG4),1), color = "blue", fontsize = 12)
sub2.text(4.94, (float(PBE0EthanolG5)-9.5), round(float(PBE0EthanolG5),1), color = "blue", fontsize = 12)

sub3.text(0.95, (float(PBE0AcetonitrilePCMG1)+3), round(float(PBE0AcetonitrilePCMG1),1), color = "cyan", fontsize = 12)
sub3.text(1.945, (float(PBE0AcetonitrilePCMG2)+3), round(float(PBE0AcetonitrilePCMG2),1), color = "cyan", fontsize = 12)
sub3.text(2.967, (float(PBE0AcetonitrilePCMG3)+3), round(float(PBE0AcetonitrilePCMG3),1), color = "cyan", fontsize = 12)
sub3.text(3.94, (float(PBE0AcetonitrilePCMG4)+3), round(float(PBE0AcetonitrilePCMG4),1), color = "cyan", fontsize = 12)
sub3.text(4.94, (float(PBE0AcetonitrilePCMG5)+3), round(float(PBE0AcetonitrilePCMG5),1), color = "cyan", fontsize = 12)

sub3.text(0.96, (float(PBE0AcetonitrileG1)-9.5), round(float(PBE0AcetonitrileG1),1), color = "blue", fontsize = 12)
sub3.text(1.96, (float(PBE0AcetonitrileG2)-9.5), round(float(PBE0AcetonitrileG2),1), color = "blue", fontsize = 12)
sub3.text(2.95, (float(PBE0AcetonitrileG3)-9.5), round(float(PBE0AcetonitrileG3),1), color = "blue", fontsize = 12)
sub3.text(3.94, (float(PBE0AcetonitrileG4)-9.5), round(float(PBE0AcetonitrileG4),1), color = "blue", fontsize = 12)
sub3.text(4.94, (float(PBE0AcetonitrileG5)-9.5), round(float(PBE0AcetonitrileG5),1), color = "blue", fontsize = 12)

#Ticks
sub1.set_xticks([])
sub2.set_xticks([])
sub3.set_xticks([])
#Limits
sub1.set_ylim([-90, 30])
sub2.set_ylim([-90, 30])
sub3.set_ylim([-90, 30])

#Ticks
sub1.set_yticks([20, 10, 0, -10, -20, -30, -40, -50, -60, -70 , -80])
sub2.set_yticks([20, 10, 0, -10, -20, -30, -40, -50, -60, -70 , -80])
sub3.set_yticks([20, 10, 0, -10, -20, -30, -40, -50, -60, -70 , -80])

#Plot titles
sub1.text(0.84, -82.5, "Water", bbox = {'facecolor': "white", "pad": 4}, fontsize = 20)
sub2.text(0.84, -82.5, "Ethanol", bbox = {'facecolor': "white", "pad": 4}, fontsize = 20)
sub3.text(0.84, -82.5, "Acetonitrile", bbox = {'facecolor': "white", "pad": 4}, fontsize = 20)

#Colour parts of plots
sub1.fill_between((1, 2), -100, 30, facecolor = "green", alpha = 0.1)
sub1.fill_between((3, 4), -100, 30, facecolor = "blue", alpha = 0.1)
sub1.fill_between((4, 5), -100, 30, facecolor = "orange", alpha = 0.1)

sub2.fill_between((1, 2), -100, 30, facecolor = "green", alpha = 0.1)
sub2.fill_between((3, 4), -100, 30, facecolor = "blue", alpha = 0.1)
sub2.fill_between((4, 5), -100, 30, facecolor = "orange", alpha = 0.1)

sub3.fill_between((1, 2), -100, 30, facecolor = "green", alpha = 0.1)
sub3.fill_between((3, 4), -100, 30, facecolor = "blue", alpha = 0.1)
sub3.fill_between((4, 5), -100, 30, facecolor = "orange", alpha = 0.1)

#Legend
PBE0Waterleg = mlines.Line2D([], [], color = "blue", linestyle = "dashed", label = "SMD")
PBE0Ethanolleg = mlines.Line2D([], [], color = "blue", linestyle = "dashed", label = "SMD")
PBE0Acetonitrileleg = mlines.Line2D([], [], color = "blue", linestyle = "dashed", label = "SMD")
PBE0WaterPCMleg = mlines.Line2D([], [], color = "cyan", linestyle = "dashed", label = "PCM")
PBE0EthanolPCMleg = mlines.Line2D([], [], color = "cyan", linestyle = "dashed", label = "PCM")
PBE0AcetonitrilePCMleg = mlines.Line2D([], [], color = "cyan", linestyle = "dashed", label = "PCM")
Waterlegends = (PBE0Waterleg, PBE0WaterPCMleg)
Ethanollegends = (PBE0Ethanolleg, PBE0EthanolPCMleg)
Acetonitrilelegends = (PBE0Acetonitrileleg, PBE0AcetonitrilePCMleg)
sub1.legend(handles=Waterlegends, loc="upper right")
sub2.legend(handles=Ethanollegends, loc="upper right")
sub3.legend(handles=Acetonitrilelegends, loc="upper right")

plt.savefig("Solvation models PBE0.png", format = "png", bbox_inches='tight', dpi = 300)
plt.show()
