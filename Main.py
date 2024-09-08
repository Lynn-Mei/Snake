#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame, sys
from FetchScores import *
from pygame.locals import *
pygame.init()
import time
clock = time.clock() 

white = (255, 255, 255) 
black = (50,51,50)
blue = (0, 0, 128)
green = (0,128,0)
green4 = (0,128,0)
orange = (180,45,0)
orange4 = (180,45,0)


Record = getScores()
but4 = "record : " + str(Record)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake menu")
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 18)
text = font.render('Snake by Luwelin', True, white, black)
text2 = font2.render('Play', True, black, green4)
text3 = font2.render("quit", True, black, orange4)
text4 = font2.render(but4, True, white, black)
textRect = text.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect.center = (800 // 2, 600 // 5)
textRect2.center = (200, 475)
textRect3.center = (600, 475)
textRect4.center = (400, 475)
crashed = False

while not crashed:
    g =1
    gameDisplay.fill(black)
    gameDisplay.blit(text, textRect)
    gameDisplay.blit(text4, textRect4)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            green4 = (255, 255, 255)
            text2 = font2.render('Play', True, black, green4)
            pygame.draw.rect(gameDisplay, white,(150,450,100,50))
            if click[0] == 1:
                print("had")
                exec(open("./Shnak2.py").read())
                print("bi")
                time.sleep(0.15)
    else:
        green4 = (0,128,0)
        text2 = font2.render('Play', True, black, green4)
        pygame.draw.rect(gameDisplay, green,(150,450,100,50))
#pl
    if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
            orange4 = (255, 255, 255)
            text3 = font2.render("quit", True, black, orange4)
            pygame.draw.rect(gameDisplay, white,(550,450,100,50))
            if click[0] == 1:
                crashed = True
                quit()
                exit()

                
    else:
        orange4 = (180,45,0)
        text3 = font2.render("quit", True, black, orange4)     
        pygame.draw.rect(gameDisplay, orange,(550,450,100,50))
    gameDisplay.blit(text2, textRect2)
    gameDisplay.blit(text3, textRect3)
    
    pygame.display.update()
    

quit()