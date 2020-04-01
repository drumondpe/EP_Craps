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

        if(inComeOut):
            print('Você está na fase Come Out')
            apostarComeOut = str(input('Você quer apostar em Pass Line Bet (sim/não)??? '))
            apostarComeOut = apostarComeOut.lower()
            
            if(apostarComeOut == "sim"):
                betComeOut = int(input('Qual valor você quer apostar? '))
            
                
        else:
            print("Você está na fase Point, seu número é {}".format(pointWin))
#Perfunta aposta FIELD    
        apostarField = str(input('Você quer apostar em Field (sim/não)??? '))
        apostarField = apostarField.lower() 

        if(apostarField == "sim"):
            inField = True
            betField = int(input('Qual valor você quer apostar? '))
        else:
            inField = False

#Pergunta aposta ANYCRAPS    
        apostarAnyCraps = str(input('Você quer apostar em AnyCraps (sim/não)??? '))
        apostarAnyCraps = apostarAnyCraps.lower() 

        if(apostarAnyCraps == "sim"):
            inAnyCraps = True
            betAnyCraps = int(input('Qual valor você quer apostar? '))
        else:
            inAnyCraps = False

#Pergunta aposta TWELVE    
        apostarTwelve = str(input('Você quer apostar em Twelve (sim/não)??? '))
        apostarTwelve = apostarTwelve.lower() 

        if(apostarTwelve == "sim"):
            inTwelve = True
            betTwelve = int(input('Qual valor você quer apostar? '))
        else:
            inTwelve = False            

        #Roda dados
        dadoUm = random.randint(1,6)
        dadoDois = random.randint(1,6)
        somaDados= dadoUm+dadoDois

        print("Sua soma foi {}".format(somaDados))

#Realiza aposta ComeOut            
        if(inComeOut):
            if True:
                if(somaDados in comeOutWin):
                    fichas += betComeOut*2
                    print ('Você ganhou 2x seu valor de aposta')
                elif(somaDados in comeOutLoss):
                    fichas -= betComeOut
                    print ('Você perdeu seu valor de aposta')
                else:
                    inComeOut = False
                    pointWin = somaDados
        else:
            if(somaDados == pointWin):
                fichas += betComeOut
                print ('Você ganhou seu valor de aposta')
                inComeOut = True
                
            elif(somaDados == pointLoss):
                fichas -= betComeOut
                print ('Você perdeu seu valor de aposta')
                inComeOut = True            

#Realiza aposta FIELD
        if(inField):
            if True:
                if(somaDados in fieldWinUm):
                    fichas += betField
                elif (somaDados in fieldWinDois):
                    fichas += betField*2
                elif (somaDados in fieldWinTres):
                    fichas += betField*3
                elif (somaDados in fieldLoss):
                    fichas -= betField
#Realiza aposta ANYCRAPS
        if(inAnyCraps):
            if True:
                if(somaDados in anyCrapsWin):
                    fichas += betAnyCraps*7
                else:
                    fichas -= betAnyCraps

#Realiza aposta TWELVE
        if(inTwelve):
            if True:
                if(somaDados in twelveWin):
                    fichas += betTwelve*30
                else:
                    fichas -= betTwelve            
                
jogo()