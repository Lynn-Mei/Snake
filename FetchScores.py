#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pickle

fileScores = "scores"

def getScores():
    if os.path.exists(fileScores):        
        folder = open(fileScores, "rb")
        depickler = pickle.Unpickler(folder)
        scores = depickler.load()
        folder.close
    else:
        scores = 0
    return scores

def saveScores(scores):
    folder = open(fileScores, 'wb')
    pickler = pickle.Pickler(folder)
    pickler.dump(scores)
    
s = getScores()
print(s)