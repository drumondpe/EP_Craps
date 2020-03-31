# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:17:57 2020

@author: Pedro Drumond
"""

#Precisamos travar o código antes da fase point e peruntar se está preparado para ela
#Ajustar o jogar de novo
#Dar as fichas

import random

def jogo()  :

    inComeOut = True
    comeOutWin = [7, 11]
    comeOutLoss = [2,3,12]
    pointWin = 0
    pointLoss = 7
    betComeOut = 0 

    inField = False
    fieldWin = [2, 3, 4, 9, 10, 11, 12]
    fieldLoss = [5, 6, 7, 8]
    betField = 0 

    inAnyCraps = False
    anyCrapsWin = [2, 3, 12]
    anyCrapsLoss = [1, 4, 5, 6, 7, 8, 9, 10, 11]
    betAnyCraps = 0 
    