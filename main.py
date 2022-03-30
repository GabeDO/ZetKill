# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:36:32 2020

@author: Gabe
"""


from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import math



chili = 0
def ChiliTracker():
     global chili
     chili = chili + 1
     if chili > 10:
         chili = 0
         setattr(KillPer_label1, 'text', 'Ratios:\n2 Bird eye chilis\n1 Sugar\n0.4 peeled garlic \n0.4 Ginger\n0.7 vinegar \nSalt\nLemon zest\nMathod:\nBlend the garlic, chilli, ginger and vinegar.\nToss it all into a pot and bring to a boil.\nAdd sugar, mix and bring to a simmer. \nAdd a bit of lemon zest and salt to taste.\n\nLet it cool, and bottle it in sterilized bottles. ')
         setattr(KillPer_label2, 'text', '')
         setattr(KillPer_label3, 'text', '')

def KillPercent(FIRE, Character, StageHeight):
    global KillPercents
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
    KillPercents = []
    for STAGE in StageHeight[2:]:
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
            if sum(Z) >= (STAGE - FirePixels):
                KillPercents.append(str(percentage - Damage) + '%')
                #print(sum(Z))
        
                break
            else:
                pass
    KillPercents.append('NA')
    KillPercents.append('NA')       
    return KillPercents
        
def SetStage(x):  
    global S
    search = x
    for sublist in StageList:
        if sublist[0] == search:
            S = sublist
            break
    setattr(Stage_Image, 'source',S[1])
    print(S)
    
def SetChar(x):  
    global C
    search = x
    for sublist in CharList:
        if sublist[2] == search:
            C = sublist
            break
    setattr(Char_Image, 'source',C[3])
    print(C)

#weight and gravity values: [Weight, Gravity]

Clairen = [1, 0.5,'Clairen','Clairen.png']
Forsburn = [1, 0.5, 'Forsburn', 'Forsburn.png']
Zetterburn = [1, 0.5,'Zetterburn','Zetterburn.png']
Sylvanos = [0.95,0.51,' Sylvanos','Sylvanos.png']
Maypul = [1.1, 0.5,'Maypul','Maypul.png']
Kragg = [0.9,0.53,'Kragg','Kragg.png']
Ori = [1.15, 0.5,'Ori','Ori.png']
ShovelKnight = [0.95,0.5,'Shovel Knight','Shovel Knight.png']
Wrastor = [1.2, 0.45,'Wrastor','Wrastor.png']
Absa = [1.1, 0.45,'Absa','Absa.png']
Elliana = [0.9, 0.45,'Elliana','Elliana.png']
EllianaOutOfMech = [1.3, 0.45,'Elliana \n Out Of Mech','EllianaOOM.png']
Orcane = [1, 0.5,'Orcane','Orcane.png']
Etalus = [0.9,0.5,'Etalus','Etalus.png']
EtalusInIce = [0.9,0.6,'Etalus \n In Ice','EtalusICE.png']
Ranno = [1.05,0.5,'Ranno','Ranno.png']
Hodan = [0.9,0.52,'Hodan', 'Hodan.png']
Mollo = [1,0.51,'Mollo', 'Mollo.png']
Olympia = [0.98,0.51,'Olympia','Olympia.png']
Pomme = [1.1,0.45,'Pomme', 'Pomme.png']

#Stage height Data

FC = ['Fire \n Capital','FC.png',612, 516, 420]
RW = ['Rock \n Wall','RW.png',580, 484, 388]
MP = ['Merchant \n Port','MP.png',596, 500, 420]    
TL = ['Treetop \n Lodge','TL.png',612, 516, 450]    
TP = ['Tempest \n Peak','TP.png',628, 596, 532]
FF = ['Frozen \n Fortress','FF.png',600, 504, 408]
TH = ['Tower \n of Heaven','TH.png',596, 500, 404]
FoF= ['Forest \n Floor','FoF.png',564, 468]
TrP= ['Troupple \n Pond','TrP.png',600, 504, 408]
AG = ['Aethereal \n Gates','AG.png',612, 500]
EA = ['Endless \n Abyss','EA.png',570]
ST = ['Spirit \n Tree','ST.png',548, 466]
AA = ['Air \n Armada','AA.png',564, 388]
BH = ['Blazing \n Hideout','BH.png',596, 468]
JV = ['Julesvale','JV.png',590, 494, 398]

C = Clairen
S = FC

CharList = [Clairen, Forsburn, Zetterburn, Sylvanos,Maypul, Kragg, Ori, ShovelKnight,Wrastor, Absa,Elliana, EllianaOutOfMech, Orcane, Etalus,EtalusInIce, Ranno, Hodan, Mollo, Olympia, Pomme]
StageList = [FC, RW, MP, TL, TP, FF, TH, FoF, TrP, AG, EA, ST, AA, BH, JV]

from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.widget import Widget
from kivy.uix.switch import Switch
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle



window_size = Window.size
Window.clearcolor = (0.2, 0.2, 0.2, 0.2)
root = Widget()

Taunt_Gif = Image(source = 'Zet.gif', anim_delay = -1,width = (Window.size[0]/1.8), height = (Window.size[0]/1.8),pos= (window_size[0]*0.6, window_size[1]/5.5))


FIRE = False

def callback(instance, value):
    global FIRE
    FIRE = value

switch = Switch(height=window_size[1]/4,width = window_size[0]/4,pos=((window_size[0]*0.5), 0))
switch.bind(active=callback)




# create a dropdown with 10 buttons
dropdown_Char = DropDown()
dropdown_Stage= DropDown()

Char_Image = Image(source = 'Orby.png',pos=(0, window_size[1]/6),height=window_size[1]/4,width = window_size[0]/4)
for Character in CharList:
    btn_Char = Button(text=Character[2], size_hint_y=None, height=(window_size[1]/8))
    btn_Char.bind(on_release =lambda btn_Char: dropdown_Char.select(btn_Char.text))
    dropdown_Char.add_widget(btn_Char)


Stage_Image = Image(source = 'Stages.png',pos=((window_size[0]*0.25), window_size[1]/7.3),height=window_size[1]/3,width = window_size[0]/4)
for Stage in StageList:
    btn_Stage = Button(text=Stage[0], size_hint_y=None, height=(window_size[1]/8))
    btn_Stage.bind(on_release=lambda btn_Stage: dropdown_Stage.select(btn_Stage.text))   
    dropdown_Stage.add_widget(btn_Stage)


mainbutton_Char = Button(text='Character', size_hint=(None, None), height=window_size[1]/4,width = window_size[0]/4,pos=(0, 0))
mainbutton_Stage = Button(text='Stage', size_hint=(None, None), height=window_size[1]/4,width = window_size[0]/4,pos=((window_size[0]*0.25), 0))

mainbutton_Char.bind(on_release=dropdown_Char.open)
mainbutton_Stage.bind(on_release=dropdown_Stage.open)

dropdown_Char.bind(on_select=lambda instance, x: setattr(mainbutton_Char, 'text', x))
dropdown_Char.bind(on_select=lambda instance, x: SetChar(x))
dropdown_Stage.bind(on_select=lambda instance, x: setattr(mainbutton_Stage, 'text', x))
dropdown_Stage.bind(on_select=lambda instance, x: SetStage(x))


RUN_Button = Button(text="RUN", size_hint_y=None, height=window_size[1]/4,width = window_size[0]/4,pos=(window_size[0]*0.75, 0))


KillPer_label1 = Label(text="Floor Kill Percent" ,pos=(window_size[0]*0.5, window_size[1]*0.7),font_size=(Window.size[0]/24))
KillPer_label2 = Label(text="Platform 1 Kill Percents",pos=(window_size[0]*0.5, window_size[1]*0.6),font_size=(Window.size[0]/24))
KillPer_label3 = Label(text="Platform 2 Kill Percents",pos=(window_size[0]*0.5, window_size[1]*0.5),font_size=(Window.size[0]/24))

RUN_Button.bind(on_press =lambda x: setattr(KillPer_label1, 'text', 'Floor Kill Percent:    ' + str(KillPercent(FIRE, C, S)[0])))
RUN_Button.bind(on_press =lambda x: setattr(KillPer_label2, 'text', 'Platform 1 Kill Percents:    ' + str(KillPercent(FIRE, C, S)[1])))
RUN_Button.bind(on_press =lambda x: setattr(KillPer_label3, 'text', 'Platform 2 Kill Percents:    ' + str(KillPercent(FIRE, C, S)[2])))
RUN_Button.bind(on_press =lambda x: setattr(Taunt_Gif, 'anim_delay', 0.07))
RUN_Button.bind(on_press =lambda x: setattr(Taunt_Gif, 'anim_loop', 1))
RUN_Button.bind(on_press =lambda x: setattr(Taunt_Gif, 'anim_delay', -1))

#chilli
RUN_Button.bind(on_release =lambda x: ChiliTracker())

#INFO
INFO_Button = Button(text="Info", size_hint_y=None, height=window_size[0]/10,width = window_size[0]/10,pos=(0, window_size[1]*0.90))
INFO_Button.bind(on_release =lambda x: setattr(KillPer_label1, 'text', 'Made by Gabe OReilly'))
INFO_Button.bind(on_release =lambda x: setattr(KillPer_label2, 'text', 'Thanks to Meance13 \n& Trevor Youngblood\nfor the help <3'))
INFO_Button.bind(on_release =lambda x: setattr(KillPer_label3, 'text', 'Join your local communist party!'))

root.add_widget(INFO_Button)

root.add_widget(Taunt_Gif)
root.add_widget(Char_Image)
root.add_widget(Stage_Image)
root.add_widget(Label(text="Fire",pos=((window_size[0]*0.58),window_size[1]/7.5),font_size=(Window.size[0]/24)))
root.add_widget(KillPer_label1)
root.add_widget(KillPer_label2)
root.add_widget(KillPer_label3)
root.add_widget(mainbutton_Char)
root.add_widget(RUN_Button)
root.add_widget(mainbutton_Stage)
root.add_widget(switch)


runTouchApp(root)

    





      
    




































