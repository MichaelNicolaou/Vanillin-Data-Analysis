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

WARNING: CODE WILL TAKE MULTIPLE MINUTES TO COMPLETE

###############################################################################
#Data process
###############################################################################
#Spreadsheet selection
sheet = ["BP86", "B3LYP", "PBE0", "M06-2X", "wB97XD", "M06"]
for f in sheet:
    #Read data   
    df = pd.read_excel("Vanillin Data.xlsx", sheet_name = f)
    
    #Organise Dataframe
    df = df.astype(float)
    df = df.round(decimals=1)
    
    #Get peak x and y values
    x = df.iloc[:,0]
    dfx = pd.Series(x).to_list()
    y = df.iloc[:,1] * -1
    dfy = pd.Series(y).to_list()
    
    #Create new arrays for all spectrum coordinates
    x = np.arange(0,4000,0.1)
    x = x.tolist()
    x = [round(elem, 1) for elem in x]
    y = [0] * 40000
    
    #Update peak y-values
    counter = -1
    for i in x:
        counter = counter + 1
        if i in dfx:
            position = dfx.index(i)
            y[counter] = dfy[position]
    
    print("First loop done")
    
    #Define peak distribution curve (Here I chose a Gaussian model,
    #alternatively it could be something else, like a Lorentzian model).
    #x corresponds to the x-value, a corresponds to y-max, b corresponds
    #to x-value for y-max and c corresponds to variance (determines width of peak)
    def gauss(x, a, b, c):
        return a * (math.e ** (-(((x - b) ** 2) / ((2 * c) ** 2))))
    
    #Iron out a weird decimal place drift (Would add extra decimals,
    # e.g. 42.01000003)
    x = [round(elem, 1) for elem in x]
    y = [round(elem, 1) for elem in y]
        
    #Smoothen lines to curves, calculate new y-coordinates using distribution 
    #model around peak x-coordinates, check if x-coordinates belong to another
    #peak and if so compare and replace with the lowest value.
    # #Debug test data
    # dfx = [0.20, 0.5]
    templist = []
    counter2 = 0
    c = 3
    
    #First loop - calculated first half of peaks
    for i in dfx:
        z = x.index(i)     
        xdata = np.array(x[(z - 500):z])
        xdatalist = xdata.tolist()
        templist.extend(xdatalist)
    for i in dfx:
        z = x.index(i)
        if y[z] >= -100:
            c = 2
        elif y[z] >= -250 and y[z] < -100:
            c = 5
        else:
            c = 7  
        xdata = np.array(x[(z - 500):z])
        for k in xdata:
            if k in templist:
                z1 = int(x.index(k))
                if gauss(k, y[z], x[z], c) < y[z1]:
                    y[z1] = gauss((k), y[z], x[z], c)
                    templist.append(k)
                    counter2 = counter2 + 1
                else:
                    continue
        
    print("Second loop done")
        
    #Second loop - calculates second half of peaks - This sequence is done to avoid peaks eating up 
    #The peaks after
    for i in dfx:
        z = x.index(i)     
        xdata = np.array(x[z:(z + 500)])
        xdatalist = xdata.tolist()
        templist.extend(xdatalist)
    for i in dfx:
        z = x.index(i)
        if y[z] >= -100:
            c = 2
        elif y[z] >= -250 and y[z] < -100:
            c = 5
        else:
            c = 7  
        xdata = np.array(x[z:(z + 500)])
        for k in xdata:
            if k in templist:
                z1 = int(x.index(k))
                if gauss(k, y[z], x[z], c) < y[z1]:
                    y[z1] = gauss((k), y[z], x[z], c)
                    templist.append(k)
                    counter2 = counter2 + 1
                else:
                    continue
                    
    print("Third loop done")

    #Lower the baseline below 0
    y = [i-2 for i in y]

    if f == "BP86":
        xBP86 = x
        yBP86 = y
    elif f == "PBE0":
        xPBE0 = x
        yPBE0 = y
    elif f == "B3LYP":
        xB3LYP = x
        yB3LYP = y
    elif f == "M06-2X":
        xM062X = x
        yM062X = y
    elif f == "wB97XD":
        xwB97XD = x
        ywB97XD = y
    elif f == "M06":
        xM06 = x
        yM06 = y   
    
    print("Functional done")
    
#Read data for expt 
df = pd.read_excel("Z:/Michael Nicolaou/Projects/Vanillin-veratric acid/Workbench.xlsx", sheet_name = "Expt")

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

###############################################################################
#Plot
###############################################################################
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

#Create subplots
sub1 = fig.add_subplot(3, 4, (1, 8))
sub2 = fig.add_subplot(3, 4, 9)
sub3 = fig.add_subplot(3, 4, 10)
sub4 = fig.add_subplot(3, 4, 11)
sub5 = fig.add_subplot(3, 4, 12)

#Adjust subplot limits
sub1.set_xlim(4000,0)
sub1.set_ylim(-420,0)

sub2.set_xlim(3900,3750)
sub2.set_ylim(-200,-100)

sub3.set_xlim(2975,2825)
sub3.set_ylim(-150,-80)

sub4.set_xlim(1850,1725)
sub4.set_ylim(-400,-250)

sub5.set_xlim(1375,1275)
sub5.set_ylim(-400,-200)

#Ticks
sub1.set_yticks([])
sub2.set_yticks([])
s2xticks = np.arange(3750, 3901, 25)
sub2.set_xticks(s2xticks)
sub3.set_yticks([])
s3xticks = np.arange(2825, 2976, 25)
sub3.set_xticks(s3xticks)
sub4.set_yticks([])
s4xticks = np.arange(1725, 1851, 25)
sub4.set_xticks(s4xticks)
sub5.set_yticks([])
s5xticks = np.arange(1275, 1376, 25)
sub5.set_xticks(s5xticks)

#Add main subplot axis labels
sub1.set_xlabel("Wavenumber ($\mathregular{cm^{-1}}$)")
sub1.set_ylabel("Transmittance")

#Plot functionals
sub1.plot(xBP86, yBP86, linewidth = 1, color = "black", alpha = 0.6)
sub1.plot(xPBE0, yPBE0, linewidth = 1, color = "blue", alpha = 0.6)  
sub1.plot(xB3LYP, yB3LYP, linewidth = 1, color = "green", alpha = 0.6)  
sub1.plot(xM062X, yM062X, linewidth = 1, color = "pink", alpha = 0.6)  
sub1.plot(xwB97XD, ywB97XD, linewidth = 1, color = "purple", alpha = 0.6)  
sub1.plot(xM06, yM06, linewidth = 1, color = "orange", alpha = 0.6)  
sub1.plot(xexpt, yexpt, linewidth = 1.5, color = "red", linestyle = ":")

sub2.plot(xBP86, yBP86, linewidth = 1, color = "black", alpha = 0.6)
sub2.plot(xPBE0, yPBE0, linewidth = 1, color = "blue", alpha = 0.6)  
sub2.plot(xB3LYP, yB3LYP, linewidth = 1, color = "green", alpha = 0.6)  
sub2.plot(xM062X, yM062X, linewidth = 1, color = "pink", alpha = 0.6)  
sub2.plot(xwB97XD, ywB97XD, linewidth = 1, color = "purple", alpha = 0.6)  
sub2.plot(xM06, yM06, linewidth = 1, color = "orange", alpha = 0.6) 

sub3.plot(xBP86, yBP86, linewidth = 1, color = "black", alpha = 0.6)
sub3.plot(xPBE0, yPBE0, linewidth = 1, color = "blue", alpha = 0.6)  
sub3.plot(xB3LYP, yB3LYP, linewidth = 1, color = "green", alpha = 0.6)  
sub3.plot(xM062X, yM062X, linewidth = 1, color = "pink", alpha = 0.6)  
sub3.plot(xwB97XD, ywB97XD, linewidth = 1, color = "purple", alpha = 0.6)  
sub3.plot(xM06, yM06, linewidth = 1, color = "orange", alpha = 0.6) 

sub4.plot(xBP86, yBP86, linewidth = 1, color = "black", alpha = 0.6)
sub4.plot(xPBE0, yPBE0, linewidth = 1, color = "blue", alpha = 0.6)  
sub4.plot(xB3LYP, yB3LYP, linewidth = 1, color = "green", alpha = 0.6)  
sub4.plot(xM062X, yM062X, linewidth = 1, color = "pink", alpha = 0.6)  
sub4.plot(xwB97XD, ywB97XD, linewidth = 1, color = "purple", alpha = 0.6)  
sub4.plot(xM06, yM06, linewidth = 1, color = "orange", alpha = 0.6) 

sub5.plot(xBP86, yBP86, linewidth = 1, color = "black", alpha = 0.6)
sub5.plot(xPBE0, yPBE0, linewidth = 1, color = "blue", alpha = 0.6)  
sub5.plot(xB3LYP, yB3LYP, linewidth = 1, color = "green", alpha = 0.6)  
sub5.plot(xM062X, yM062X, linewidth = 1, color = "pink", alpha = 0.6)  
sub5.plot(xwB97XD, ywB97XD, linewidth = 1, color = "purple", alpha = 0.6)  
sub5.plot(xM06, yM06, linewidth = 1, color = "orange", alpha = 0.6) 

#Add colour to main subplot zoom-in ranges
sub1.fill_between((3900, 3750), -420, 0, facecolor = "green", alpha = 0.1)
sub1.fill_between((2975, 2825), -420, 0, facecolor = "blue", alpha = 0.1)
sub1.fill_between((1850, 1725), -420, 0, facecolor = "orange", alpha = 0.1)
sub1.fill_between((1375, 1275), -420, 0, facecolor = "red", alpha = 0.1)

#Add connector patches
con1left = ConnectionPatch(xyA = (3900, -150), coordsA = sub1.transData, xyB = (3900, -100), coordsB = sub2.transData, color = "black", alpha = 0.5, linewidth = 0.5)
con1right = ConnectionPatch(xyA = (3750, -150), coordsA = sub1.transData, xyB = (3750, -100), coordsB = sub2.transData, color = "black", alpha = 0.5, linewidth = 0.5)

fig.add_artist(con1left)
fig.add_artist(con1right)
                            
con2left = ConnectionPatch(xyA = (2975, -115), coordsA = sub1.transData, xyB = (2975, -80), coordsB = sub3.transData, color = "black", alpha = 0.5, linewidth = 0.5)
con2right = ConnectionPatch(xyA = (2825, -115), coordsA = sub1.transData, xyB = (2825, -80), coordsB = sub3.transData, color = "black", alpha = 0.5, linewidth = 0.5)

fig.add_artist(con2left)
fig.add_artist(con2right)

con3left = ConnectionPatch(xyA = (1850, -300), coordsA = sub1.transData, xyB = (1850, -250), coordsB = sub4.transData, color = "black", alpha = 0.5, linewidth = 0.5)
con3right = ConnectionPatch(xyA = (1725, -300), coordsA = sub1.transData, xyB = (1725, -250), coordsB = sub4.transData, color = "black", alpha = 0.5, linewidth = 0.5)

fig.add_artist(con3left)
fig.add_artist(con3right)

con4left = ConnectionPatch(xyA = (1375, -250), coordsA = sub1.transData, xyB = (1375, -200), coordsB = sub5.transData, color = "black", alpha = 0.5, linewidth = 0.5)
con4right = ConnectionPatch(xyA = (1275, -250), coordsA = sub1.transData, xyB = (1275, -200), coordsB = sub5.transData, color = "black", alpha = 0.5, linewidth = 0.5)

fig.add_artist(con4left)
fig.add_artist(con4right)

#Legends
BP86leg = mlines.Line2D([], [], color = "black", label = "BP86")
PBE0leg = mlines.Line2D([], [], color = "blue", label = "PBE0")
B3LYPleg = mlines.Line2D([], [], color = "green", label = "B3LYP")
M062Xleg = mlines.Line2D([], [], color = "pink", label = "M06-2X")
wB97XDleg = mlines.Line2D([], [], color = "purple", label = "wB97XD")
M06leg = mlines.Line2D([], [], color = "orange", label = "M06")
exptleg = mlines.Line2D([], [], color = "red", linestyle = ":", label = "Expt")
legends = (BP86leg, PBE0leg, B3LYPleg, M062Xleg, wB97XDleg, M06leg, exptleg)
sub1.legend(handles=legends, loc="upper right")

#Save figure
fig.savefig("Combined peaks.png", format = "png", bbox_inches='tight', dpi = 300)
plt.show    