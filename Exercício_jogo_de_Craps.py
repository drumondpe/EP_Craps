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
    fieldWinUm = [3, 4, 9, 10, 11] #ganha o valor que apostou
    fieldWinDois = [2] #ganha o dobro do que apostou
    fieldWinTres = [12] #ganha o triplo
    fieldLoss = [5, 6, 7, 8] #perde tudo
    betField = 0 

    inAnyCraps = False
    anyCrapsWin = [2, 3, 12] #7x o que apostou
    anyCrapsLoss = [1, 4, 5, 6, 7, 8, 9, 10, 11] #perde o que apostou
    betAnyCraps = 0 

    inTwelve = False
    twelveWin = [12] 
    twelveCrapsLoss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    betTwelve = 0

    fichas = 1000
    
    jogando=True
    resposta=input('Você quer jogar (sim/não)? ')       
    if resposta=='não':
        jogando=False 
    while(jogando):

        print('Você começou a jogar!')
        print("Você tem {} fichas".format(fichas))