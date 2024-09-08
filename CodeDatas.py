#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
from random import *

class Leni:
    """Classe définissant un leni caractérisée par :
    - Nombre
    - position x
    - position y
    ...
    """
    
    def __init__(self, LenTag, LenX, LenY):
        """Constructeur de notre classe"""
        self.LenTag = LenTag
        self.LenX = LenX
        self.LenY = LenY
        
class Plenio:
    """Classe definissant le es caracterisiques du snake controlle"""
    def __init__(self, Lenis, Head):
        self.Head = Head
        self.Lenis = Lenis
        
black = (0,0,0)
white = (255,255,255)
green = (50,230,0)
green2 = (75,255,0)
red= (255,75,0)

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


x=400
y=300
x1=425
y1=300
x2=450
y2=300
p=0
p1=0
p2=0
d2=0
d1=0
d=0
lenght = 3
direction="left"
direction2="l"
stade = 0