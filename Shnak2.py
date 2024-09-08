#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
from random import *
from FetchScores import *
from CodeDatas import *
import time
pygame.init()
pygame.mixer.init()
print("a")

Record = getScores()
class Leni:
    def __init__(self, LenTag, LenX, LenY, dire, prev):
        """Constructeur de notre classe"""
        self.LenTag = LenTag
        self.LenX = LenX
        self.LenY = LenY
        self.dire = dire
        self.prev = prev
    def __repr__(self):
        return "Personne: X: ({}), Direction: ({}), Prev: ({})".format(
                self.LenTag, self.dire, self.prev)

class Lenin:
    def __init__(self,Head,Body):
        self.Head = Head
        self.Body = Body

def fruitloc():
    rand1=0
    randx = []
    randy = []
    while rand1 < 800:
        randx.append(rand1)
        rand1+=25
    rand1=0
    while rand1 < 600:
        randy.append(rand1)
        rand1+=25
    value1 = randint(0, 23)
    value2 = randint(0, 31)
    value1 = randy[value1]
    value2 = randx[value2]
    values=[value2,value1]
    return values

def randcolor():
    va = randint(0, 255)
    va1 = randint(0, 255)
    va2 = randint(0, 255)
    color = (va,va1,va2)
    return color

black = (50,51,50)
black2 = (50,51,50)
white = (255,255,255)
green = (50,230,0)
green2 = (75,255,0)
red= (255,75,0)

colors = [black,black]
for i in range(0,3):
    c = randcolor()
    colors.append(c)

values=fruitloc()
value1=values[1]
value2=values[0]
        
Head = Leni(1,400,300,"left","left")
listLenis = [Head]
Leni2 = Leni(2,425,300,"left","left")
listLenis.append(Leni2)
Leni2 = Leni(3,450,300,"left","left")
listLenis.append(Leni2)
Leni2 = Leni(4,475,300,"left","left")
listLenis.append(Leni2)
j = Leni2

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('snake')

font = pygame.font.Font('freesansbold.ttf', 54)
text = font.render('Game Over', True, red, black)
textRect = text.get_rect()
textRect.center = (800 // 2, 600 // 2)

lenght = 3
pre = "None"

Score = 0

crashed = False

while not crashed:
    gameDisplay.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        Head.prev = Head.dire
        if event.type == pygame.KEYDOWN:
            Head = listLenis[0]
            if event.key == pygame.K_LEFT:
                if Head.dire != "right":
                    Head.dire = "left"
            if event.key == pygame.K_RIGHT:
                if Head.dire != "left":
                    Head.dire = "right"
            if event.key == pygame.K_UP:
                if Head.dire != "down":
                    Head.dire = "top"
            if event.key == pygame.K_DOWN:
                if Head.dire != "top":
                    Head.dire = "down"                
    gameDisplay.fill(black)
    for i in listLenis:         
        if i.LenTag != 1 :
            previous = listLenis[i.LenTag-2]
            i.prev = i.dire
            i.dire = previous.prev
        else:
            pass
        if i.dire == "left":
            i.LenX= i.LenX-25
            pygame.draw.rect(gameDisplay , colors[i.LenTag], [i.LenX,i.LenY,25,25])      
        if i.dire == "right":
            i.LenX= i.LenX+25
            pygame.draw.rect(gameDisplay , colors[i.LenTag], [i.LenX,i.LenY,25,25]) 
        if i.dire == "top":
            i.LenY= i.LenY-25
            pygame.draw.rect(gameDisplay , colors[i.LenTag], [i.LenX,i.LenY,25,25]) 
        if i.dire == "down":
            i.LenY= i.LenY+25
            pygame.draw.rect(gameDisplay , colors[i.LenTag], [i.LenX,i.LenY,25,25])
    
        Lenii = listLenis[1]
    
        if i.LenTag != 1 and i.LenTag != 2:
            print(i.LenTag)
            if Lenii.LenX == i.LenX and Lenii.LenY == i.LenY:
                print(i)
                gameDisplay.blit(text, textRect)
                pygame.display.update()
                if Score > Record:
                    Record = Score
                    saveScores(Record)
                time.sleep(2)
                crashed = True
                exec(open("./Main.py").read())

            Lenii2 = listLenis[1]
            if Lenii2.LenY < -1 or Lenii2.LenY > 600 or Lenii2.LenX < -1 or Lenii2.LenX > 800:
                gameDisplay.blit(text, textRect)
                pygame.display.update()
                if Score > Record:
                    Record = Score
                    saveScores(Record)         
                time.sleep(2)
                crashed = True
                exec(open("./Main.py").read())

  
        
    pygame.draw.rect(gameDisplay , red, [value2,value1,25,25])
    Lenii = listLenis[1]
    if Lenii.LenX == value2 and Lenii.LenY == value1:
        values=fruitloc()
        value1=values[1]
        value2=values[0]
        lastleni = listLenis[len(listLenis)-1]
        Newtag = lastleni.LenTag +1
        c = randcolor()
        colors.append(c)
        if lastleni.dire == "left" :
            NewX = lastleni.LenX+25
            NewY = lastleni.LenY
            NewDire = "left"
        if lastleni.dire == "right" :
            NewX = lastleni.LenX-25
            NewY = lastleni.LenY
            NewDire = "right"
        if lastleni.dire == "top" :
            NewX = lastleni.LenX
            NewY = lastleni.LenY+25
            NewDire = "top"
        if lastleni.dire == "down" :
            NewX = lastleni.LenX
            NewY = lastleni.LenY-25
            NewDire = "down"
        Score +=1
        Leni2 = Leni(Newtag,NewX,NewY,NewDire,NewDire)
        listLenis.append(Leni2)
        print(Score)
    Zwei = listLenis[1]
    if Head.dire == "top" and Zwei.dire == "top":
        if Head.LenY != Zwei.LenY-25 or Head.LenX != Zwei.LenX:
            pass
        

    pygame.display.update()
    time.sleep(0.10)
pygame.quit()
quit()