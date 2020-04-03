# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:36:32 2020

@author: Gabe
"""


import math
#USmash

def KillPercent(FIRE, Character, StageHeight):
    if FIRE == True:
        Damage = 7+8
        KBS = 1.3
        FirePixels = 42
        BKB = 8
    else:
        Damage = 7
        BKB = 8
        KBS = 1.1
        FirePixels = 0
    for percentage in range(300):
        FKB = BKB + KBS * Character[0] * percentage * 0.12
        Z = []
        X = FKB * math.sin(math.radians(108))
        for i in range(70):
            if X < 0:
                break
            else:
                Z.append(X)
                X = X - Character[1]
        if sum(Z) >= (StageHeight - FirePixels):
            print(percentage - Damage)
            #print(sum(Z))
    
            break
        else:
            pass




      
    
#weight and gravity values: [Weight, Gravity]
Clairen = [1, 0.5]
Forsburn = [1, 0.5]
Zetterburn = [1, 0.5]
Sylvanos = [0.95,0.51]
Maypul = [1.1, 0.5]
Kragg = [0.9,0.53]
Ori = [1.15, 0.5]
ShovelKnight = [0.95,0.5]
Wrastor = [1.2, 0.45]
Absa = [1.1, 0.45]
Elliana = [0.9, 0.45]
EllianaOutOfMech = [1.3, 0.45]
Orcane = [1, 0.5]
Etalus = [0.9,0.5]
EtalusInIce = [0.9,0.6]
Ranno = [1.05,0.5]

#Stage height Data

FC_F = 612
FC_P1 = FC_F - 96
FC_P2 = FC_F - 192

RW_F = 580
RW_P1 = RW_F - 96
RW_P2 = RW_F - 192
  
MP_F = 596
MP_P1 = MP_F - 96
MP_P2 = MP_F - 176
    
TL_F = 612
TL_P1 = TL_F - 96
TL_P2 = TL_F - 162
    
TP_F = 628
TP_P1 = TP_F - 32
TP_P2 = TP_F - 96   

FF_F = 600
FF_P1 = FF_F - 96
FF_P2 = FF_F - 192

TH_F = 596
TH_P1 = TH_F - 96
TH_P2 = TH_F - 192

FoF_F = 564
FoF_P1 = FoF_F - 96

TrP_F = 600
TrP_P1 = TrP_F - 96
TrP_P2 = TrP_F - 192

AG_F = 612
AG_P1 = AG_F - 112

 
EA_F = 570

ST_F = 548
ST_P1 = ST_F - 82

AA_F = 564
AA_P1 = AA_F - 176

BH_F = 596
BH_P1 = BH_F - 128

JV_F = 590
JV_P1 = JV_F - 96
JV_P2 = JV_F - 192



