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