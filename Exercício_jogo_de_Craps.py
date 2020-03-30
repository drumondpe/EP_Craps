# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:17:57 2020

@author: Pedro Drumond
"""

#Precisamos travar o código antes da fase point e peruntar se está preparado para ela
#Ajustar o Come Out
#Dar as fichas

import random

jogadaUm = 0


def jogo()  :
    RespostaSimNao = str(input('Você quer jogar nosso maravilhoso Craps (sim/não)??? '))
    RespostaSimNao = RespostaSimNao.lower()
    fichas = 100
    RespostaFichas = int(input('Quantas fichas você quer apostar? '))
    
    
    while RespostaSimNao == 'sim':
        print ('Você está na fase: Come Out')
        dadoUm = random.randint(1,6)
        dadoDois = random.randint(1,6)
        SomaDados= dadoUm+dadoDois
        print ("Você tirou", SomaDados)
        
        if SomaDados in [2, 3, 12]:
            RespostaSimNao = str(input('Você já perdeu?! Quer jogar de novo??? '))
            RespostaSimNao = RespostaSimNao.lower()
            
        elif SomaDados in [7, 11]:
            RespostaSimNao = str(input('Você venceu! Não quer tentar a sorte de novo? '))
            RespostaSimNao = RespostaSimNao.lower()
            
#19-28 pertencem a jogada "Come Out"
          
        else:
            jogadaUm == SomaDados
            print ('Você está na fase: Point')
            
            while RespostaSimNao == 'sim':
                dadoUm = random.randint(1,6)
                dadoDois = random.randint(1,6)
                SomaDados= dadoUm + dadoDois
                print ('Você tirou', SomaDados) 
                
                if SomaDados in [2, 3, 7 ,11 ,12]:
                    RespostaSimNao = str(input('Você já perdeu?! Quer jogar de novo??? '))
                    RespostaSimNao = RespostaSimNao.lower()
                
                
                elif SomaDados == jogadaUm:
                    RespostaSimNao = str(input('Você venceu! Não quer tentar a sorte de novo? '))
                    RespostaSimNao = RespostaSimNao.lower()
                    
                else:
                    RespostaSimNao == 'sim'
                    
                    
#36-50 pertencem a jogada "Point"
    print ('Esperamos que tenha gostado de jogar!')
jogo()   



   