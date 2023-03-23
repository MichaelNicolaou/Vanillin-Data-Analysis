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
sheet = ("Gibbs (Water) (SMD)", "Gibbs (Ethanol) (SMD)", "Gibbs (Acetonitrile) (SMD)")
for i in sheet:    
    df = pd.read_excel("Vanillin Data.xlsx", sheet_name=i, index_col="Functional")
    
    dfM06 = df.iloc[41:48, 1:15]
    
    #Equation for element-wise multiplication (coefficient * energy of molecule)
    def Gibbs_step(x, y):
        G = x*y
        return sum(G)
    
    
    ###########################################################################
    #Databases
    ###########################################################################
    ######
    #M06#
    ######
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
             
    if i == "Gibbs (Water) (SMD)":
        M06WaterG = M06G
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
        M06EthanolG = M06G
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
        M06AcetonitrileG = M06G
        M06AcetonitrileG1 = M06G1
        M06AcetonitrileG2 = M06G2
        M06AcetonitrileG3 = M06G3
        M06AcetonitrileG4 = M06G4
        M06AcetonitrileG5 = M06G5
        
        M06AcetonitrileDG1 = M06DG1
        M06AcetonitrileDG2 = M06DG2
        M06AcetonitrileDG3 = M06DG3
        M06AcetonitrileDG4 = M06DG4

#Read excel spreadsheet
sheet = ("Gibbs (Water)", "Gibbs (Ethanol)", "Gibbs (Acetonitrile)")
for i in sheet:

    df = pd.read_excel("Z:/Michael Nicolaou/Projects/Vanillin-veratric acid/Workbench.xlsx", sheet_name=i, index_col="Functional")
    
    dfM06 = df.iloc[41:48, 1:15]
    
    #Equation for element-wise multiplication (coefficient * energy of molecule)
    def Gibbs_step(x, y):
        G = x*y
        return sum(G)
    
    ###########################################################################
    #Databases
    ###########################################################################
    ######
    #M06#
    ######
    #Collect each step as a list of coefficients and the energies as a seperate list
    step_1_M06 = pd.to_numeric(dfM06.iloc[0, :])
    step_2_M06 = pd.to_numeric(dfM06.iloc[1, :])
    step_3_M06 = pd.to_numeric(dfM06.iloc[2, :])
    step_4_M06 = pd.to_numeric(dfM06.iloc[3, :])
    step_5_M06 = pd.to_numeric(dfM06.iloc[4, :])
    # M06energy = pd.to_numeric(dfM06.iloc[5, :])
    M06energy = pd.to_numeric(dfM06.iloc[6, :])

    #Find relative energy level for each reaction step
    if i == "Gibbs (Water)":
        M06G = Gibbs_step(step_1_M06, M06energy)
        M06G1 = (Gibbs_step(step_1_M06, M06energy)) - M06WaterG
        M06G2 = Gibbs_step(step_2_M06, M06energy) - M06WaterG
        M06G3 = Gibbs_step(step_3_M06, M06energy) - M06WaterG
        M06G4 = Gibbs_step(step_4_M06, M06energy) - M06WaterG
        M06G5 = Gibbs_step(step_5_M06, M06energy) - M06WaterG
    elif i == "Gibbs (Ethanol)":
        M06G = Gibbs_step(step_1_M06, M06energy)
        M06G1 = (Gibbs_step(step_1_M06, M06energy)) - M06EthanolG
        M06G2 = Gibbs_step(step_2_M06, M06energy) - M06EthanolG
        M06G3 = Gibbs_step(step_3_M06, M06energy) - M06EthanolG
        M06G4 = Gibbs_step(step_4_M06, M06energy) - M06EthanolG
        M06G5 = Gibbs_step(step_5_M06, M06energy) - M06EthanolG
    elif i == "Gibbs (Acetonitrile)":
        M06G = Gibbs_step(step_1_M06, M06energy)
        M06G1 = (Gibbs_step(step_1_M06, M06energy)) - M06AcetonitrileG
        M06G2 = Gibbs_step(step_2_M06, M06energy) - M06AcetonitrileG
        M06G3 = Gibbs_step(step_3_M06, M06energy) - M06AcetonitrileG
        M06G4 = Gibbs_step(step_4_M06, M06energy) - M06AcetonitrileG
        M06G5 = Gibbs_step(step_5_M06, M06energy) - M06AcetonitrileG
        
    #Find energy difference for each reaction step
    M06DG1 = round((M06G2 - M06G1),2)
    M06DG2 = round((M06G3 - M06G2),2)
    M06DG3 = round((M06G4 - M06G3),2)
    M06DG4 = round((M06G5 - M06G4),2)

    if i == "Gibbs (Water)":
        M06WaterPCMG = M06G
        M06WaterPCMG1 = M06G1
        M06WaterPCMG2 = M06G2
        M06WaterPCMG3 = M06G3
        M06WaterPCMG4 = M06G4
        M06WaterPCMG5 = M06G5
       
        M06WaterPCMDG1 = M06DG1
        M06WaterPCMDG2 = M06DG2
        M06WaterPCMDG3 = M06DG3
        M06WaterPCMDG4 = M06DG4
        
    elif i == "Gibbs (Ethanol)":
        M06EthanolPCMG1 = M06G1
        M06EthanolPCMG2 = M06G2
        M06EthanolPCMG3 = M06G3
        M06EthanolPCMG4 = M06G4
        M06EthanolPCMG5 = M06G5
        
        M06EthanolPCMDG1 = M06DG1
        M06EthanolPCMDG2 = M06DG2
        M06EthanolPCMDG3 = M06DG3
        M06EthanolPCMDG4 = M06DG4

    elif i == "Gibbs (Acetonitrile)":
        M06AcetonitrilePCMG1 = M06G1
        M06AcetonitrilePCMG2 = M06G2
        M06AcetonitrilePCMG3 = M06G3
        M06AcetonitrilePCMG4 = M06G4
        M06AcetonitrilePCMG5 = M06G5
        
        M06AcetonitrilePCMDG1 = M06DG1
        M06AcetonitrilePCMDG2 = M06DG2
        M06AcetonitrilePCMDG3 = M06DG3
        M06AcetonitrilePCMDG4 = M06DG4
        
###############################################################################
#Plots
###############################################################################
#Define axes
xaxis = (1, 2, 3, 4, 5)
M06Wateryaxis = (M06WaterG1, M06WaterG2, M06WaterG3, M06WaterG4, M06WaterG5)
M06Ethanolyaxis = (M06EthanolG1, M06EthanolG2, M06EthanolG3, M06EthanolG4, M06EthanolG5)
M06Acetonitrileyaxis = (M06AcetonitrileG1, M06AcetonitrileG2, M06AcetonitrileG3, M06AcetonitrileG4, M06AcetonitrileG5)
M06WaterPCMyaxis = (M06WaterPCMG1, M06WaterPCMG2, M06WaterPCMG3, M06WaterPCMG4, M06WaterPCMG5)
M06EthanolPCMyaxis = (M06EthanolPCMG1, M06EthanolPCMG2, M06EthanolPCMG3, M06EthanolPCMG4, M06EthanolPCMG5)
M06AcetonitrilePCMyaxis = (M06AcetonitrilePCMG1, M06AcetonitrilePCMG2, M06AcetonitrilePCMG3, M06AcetonitrilePCMG4, M06AcetonitrilePCMG5)


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
sub1.scatter(xaxis, M06Wateryaxis, s = 2000, c = "orange", marker = "_", linewidths = 3)
sub1.scatter(xaxis, M06WaterPCMyaxis, s = 2000, c = "red", marker = "_", linewidths = 3)

sub2.scatter(xaxis, M06Ethanolyaxis, s = 2000, c = "orange", marker = "_", linewidths = 3)
sub2.scatter(xaxis, M06EthanolPCMyaxis, s = 2000, c = "red", marker = "_", linewidths = 3)

sub3.scatter(xaxis, M06Acetonitrileyaxis, s = 2000, c = "orange", marker = "_", linewidths = 3)
sub3.scatter(xaxis, M06AcetonitrilePCMyaxis, s = 2000, c = "red", marker = "_", linewidths = 3)

#Energy change line
sub1.plot((1.08, 1.92), (M06WaterG1, M06WaterG2), c = "orange", linestyle = "dashed")
sub1.plot((2.08, 2.92), (M06WaterG2, M06WaterG3), c = "orange", linestyle = "dashed")
sub1.plot((3.08, 3.92), (M06WaterG3, M06WaterG4), c = "orange", linestyle = "dashed")
sub1.plot((4.08, 4.92), (M06WaterG4, M06WaterG5), c = "orange", linestyle = "dashed")

sub1.plot((1.08, 1.92), (M06WaterPCMG1, M06WaterPCMG2), c = "red", linestyle = "dashed")
sub1.plot((2.08, 2.92), (M06WaterPCMG2, M06WaterPCMG3), c = "red", linestyle = "dashed")
sub1.plot((3.08, 3.92), (M06WaterPCMG3, M06WaterPCMG4), c = "red", linestyle = "dashed")
sub1.plot((4.08, 4.92), (M06WaterPCMG4, M06WaterPCMG5), c = "red", linestyle = "dashed")

sub2.plot((1.08, 1.92), (M06EthanolG1, M06EthanolG2), c = "orange", linestyle = "dashed")
sub2.plot((2.08, 2.92), (M06EthanolG2, M06EthanolG3), c = "orange", linestyle = "dashed")
sub2.plot((3.08, 3.92), (M06EthanolG3, M06EthanolG4), c = "orange", linestyle = "dashed")
sub2.plot((4.08, 4.92), (M06EthanolG4, M06EthanolG5), c = "orange", linestyle = "dashed")

sub2.plot((1.08, 1.92), (M06EthanolPCMG1, M06EthanolPCMG2), c = "red", linestyle = "dashed")
sub2.plot((2.08, 2.92), (M06EthanolPCMG2, M06EthanolPCMG3), c = "red", linestyle = "dashed")
sub2.plot((3.08, 3.92), (M06EthanolPCMG3, M06EthanolPCMG4), c = "red", linestyle = "dashed")
sub2.plot((4.08, 4.92), (M06EthanolPCMG4, M06EthanolPCMG5), c = "red", linestyle = "dashed")

sub3.plot((1.08, 1.92), (M06AcetonitrileG1, M06AcetonitrileG2), c = "orange", linestyle = "dashed")
sub3.plot((2.08, 2.92), (M06AcetonitrileG2, M06AcetonitrileG3), c = "orange", linestyle = "dashed")
sub3.plot((3.08, 3.92), (M06AcetonitrileG3, M06AcetonitrileG4), c = "orange", linestyle = "dashed")
sub3.plot((4.08, 4.92), (M06AcetonitrileG4, M06AcetonitrileG5), c = "orange", linestyle = "dashed")

sub3.plot((1.08, 1.92), (M06AcetonitrilePCMG1, M06AcetonitrilePCMG2), c = "red", linestyle = "dashed")
sub3.plot((2.08, 2.92), (M06AcetonitrilePCMG2, M06AcetonitrilePCMG3), c = "red", linestyle = "dashed")
sub3.plot((3.08, 3.92), (M06AcetonitrilePCMG3, M06AcetonitrilePCMG4), c = "red", linestyle = "dashed")
sub3.plot((4.08, 4.92), (M06AcetonitrilePCMG4, M06AcetonitrilePCMG5), c = "red", linestyle = "dashed")

#Plot font
plt.rcParams['font.family'] = "serif"
plt.rcParams.update({'font.size': 18})

#Axis labels
sub1.set_ylabel("Gibbs free energy (kcal mol$^{-1}$)", fontsize = 12)
sub2.set_ylabel("Gibbs free energy (kcal mol$^{-1}$)", fontsize = 12)
sub3.set_ylabel("Gibbs free energy (kcal mol$^{-1}$)", fontsize = 12)

#Scatter labels
sub1.text(0.95, (float(M06WaterPCMG1)+3), round(float(M06WaterPCMG1),1), color = "red", fontsize = 12)
sub1.text(1.945, (float(M06WaterPCMG2)+3), round(float(M06WaterPCMG2),1), color = "red", fontsize = 12)
sub1.text(2.965, (float(M06WaterPCMG3)+3), round(float(M06WaterPCMG3),1), color = "red", fontsize = 12)
sub1.text(3.94, (float(M06WaterPCMG4)+3), round(float(M06WaterPCMG4),1), color = "red", fontsize = 12)
sub1.text(4.94, (float(M06WaterPCMG5)+3), round(float(M06WaterPCMG5),1), color = "red", fontsize = 12)

sub1.text(0.96, (float(M06WaterG1)-9.5), round(float(M06WaterG1),1), color = "orange", fontsize = 12)
sub1.text(1.96, (float(M06WaterG2)-9.5), round(float(M06WaterG2),1), color = "orange", fontsize = 12)
sub1.text(2.95, (float(M06WaterG3)-9.5), round(float(M06WaterG3),1), color = "orange", fontsize = 12)
sub1.text(3.94, (float(M06WaterG4)-9.5), round(float(M06WaterG4),1), color = "orange", fontsize = 12)
sub1.text(4.94, (float(M06WaterG5)-9.5), round(float(M06WaterG5),1), color = "orange", fontsize = 12)

sub2.text(0.95, (float(M06EthanolPCMG1)+3), round(float(M06EthanolPCMG1),1), color = "red", fontsize = 12)
sub2.text(1.945, (float(M06EthanolPCMG2)+3), round(float(M06EthanolPCMG2),1), color = "red", fontsize = 12)
sub2.text(2.945, (float(M06EthanolPCMG3)+3), round(float(M06EthanolPCMG3),1), color = "red", fontsize = 12)
sub2.text(3.94, (float(M06EthanolPCMG4)+3), round(float(M06EthanolPCMG4),1), color = "red", fontsize = 12)
sub2.text(4.94, (float(M06EthanolPCMG5)+3), round(float(M06EthanolPCMG5),1), color = "red", fontsize = 12)

sub2.text(0.96, (float(M06EthanolG1)-9.5), round(float(M06EthanolG1),1), color = "orange", fontsize = 12)
sub2.text(1.96, (float(M06EthanolG2)-9.5), round(float(M06EthanolG2),1), color = "orange", fontsize = 12)
sub2.text(2.95, (float(M06EthanolG3)-9.5), round(float(M06EthanolG3),1), color = "orange", fontsize = 12)
sub2.text(3.94, (float(M06EthanolG4)-9.5), round(float(M06EthanolG4),1), color = "orange", fontsize = 12)
sub2.text(4.94, (float(M06EthanolG5)-9.5), round(float(M06EthanolG5),1), color = "orange", fontsize = 12)

sub3.text(0.96, (float(M06AcetonitrilePCMG1)+3), round(float(M06AcetonitrilePCMG1),1), color = "red", fontsize = 12)
sub3.text(1.945, (float(M06AcetonitrilePCMG2)+3), round(float(M06AcetonitrilePCMG2),1), color = "red", fontsize = 12)
sub3.text(2.945, (float(M06AcetonitrilePCMG3)+3), round(float(M06AcetonitrilePCMG3),1), color = "red", fontsize = 12)
sub3.text(3.94, (float(M06AcetonitrilePCMG4)+3), round(float(M06AcetonitrilePCMG4),1), color = "red", fontsize = 12)
sub3.text(4.94, (float(M06AcetonitrilePCMG5)+3), round(float(M06AcetonitrilePCMG5),1), color = "red", fontsize = 12)

sub3.text(0.96, (float(M06AcetonitrileG1)-9.5), round(float(M06AcetonitrileG1),1), color = "orange", fontsize = 12)
sub3.text(1.96, (float(M06AcetonitrileG2)-9.5), round(float(M06AcetonitrileG2),1), color = "orange", fontsize = 12)
sub3.text(2.96, (float(M06AcetonitrileG3)-9.5), round(float(M06AcetonitrileG3),1), color = "orange", fontsize = 12)
sub3.text(3.94, (float(M06AcetonitrileG4)-9.5), round(float(M06AcetonitrileG4),1), color = "orange", fontsize = 12)
sub3.text(4.94, (float(M06AcetonitrileG5)-9.5), round(float(M06AcetonitrileG5),1), color = "orange", fontsize = 12)

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
M06Waterleg = mlines.Line2D([], [], color = "orange", linestyle = "dashed", label = "SMD")
M06Ethanolleg = mlines.Line2D([], [], color = "orange", linestyle = "dashed", label = "SMD")
M06Acetonitrileleg = mlines.Line2D([], [], color = "orange", linestyle = "dashed", label = "SMD")
M06WaterPCMleg = mlines.Line2D([], [], color = "red", linestyle = "dashed", label = "PCM")
M06EthanolPCMleg = mlines.Line2D([], [], color = "red", linestyle = "dashed", label = "PCM")
M06AcetonitrilePCMleg = mlines.Line2D([], [], color = "red", linestyle = "dashed", label = "PCM")
Waterlegends = (M06Waterleg, M06WaterPCMleg)
Ethanollegends = (M06Ethanolleg, M06EthanolPCMleg)
Acetonitrilelegends = (M06Acetonitrileleg, M06AcetonitrilePCMleg)
sub1.legend(handles=Waterlegends, loc="upper right")
sub2.legend(handles=Ethanollegends, loc="upper right")
sub3.legend(handles=Acetonitrilelegends, loc="upper right")

plt.savefig("Solvation models M06.png", format = "png", bbox_inches='tight', dpi = 300)
plt.show()
