# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:13:35 2020

@author: HanhNG

Attention: Changez la valeur de `dir` avant de lancer ce programme

"""

import pandas as pd
dir="D:/CDI/Cways/"

# Importer les éléments de base (instruction_list & universe)

instruction=pd.read_csv(dir+"instruction_list.txt", sep=',', header=None)
instruction.columns=["direction","step"]

universe=pd.read_csv(dir+"universe.txt", sep=':', header=None, index_col=0)
universe=universe.transpose()

# Initier la position du robot B-VZXR
nb_instruction=instruction.shape[0]
orientation="upward"
x=0
y=0
position=list()
ori=[]

def moving(move,axe, affect):
    if 0<=move<axe:
        return move
    elif move<0:
        return 0
    elif move>=axe:
        return axe

# Comme la direction change à chaque étape, on utilise des conditions pour calculer sa position. 

for i in range(nb_instruction):
    if (orientation=="upward" and instruction.direction[i]=="right") | (orientation=="downward" and instruction.direction[i]=="left"):
        move=x+instruction.step[i]
        orientation="right"
        axe=universe.width.values-1
        x=moving(move,axe,x)
    elif (orientation=="upward" and instruction.direction[i]=="left") | (orientation=="downward" and instruction.direction[i]=="right"):
        move=x-instruction.step[i]
        orientation="left"
        axe=universe.width.values-1
        x=moving(move,axe,x)
    elif (orientation=="right" and instruction.direction[i]=="left") | (orientation=="left" and instruction.direction[i]=="right"):
        move=y+instruction.step[i]
        orientation="upward"
        axe=universe.height.values-1
        y=moving(move,axe,y)
    elif (orientation=="right" and instruction.direction[i]=="right") | (orientation=="left" and instruction.direction[i]=="left"):
        move=y-instruction.step[i]
        orientation="downward"
        axe=universe.height.values-1
        y=moving(move,axe,y)
    position.append((x,y))
    ori.append(orientation)
coord=pd.Series(position)
ori1=pd.Series(ori)
result=pd.concat([instruction,coord,ori1], axis=1) #Concaténer les 2 séries pour faciliter la vérification des résultats

# La position finale de B-VZXR

print('B-VZXR est arrivé à sa destination! Sa position finale est:',(int(x),int(y)))

