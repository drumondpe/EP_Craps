# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:17:57 2020

@author: Pedro Drumond
"""

import random
jogadaUm=0


def jogo():
    RespostaSimNao = str(input('Você quer jogar nosso maravilhoso Craps (sim/não)???'))
    RespostaSimNao = RespostaSimNao.lower()
    
    while RespostaSimNao == 'sim':
        dadoUm = random.randint(1,6)
        dadoDois = random.randint(1,6)
        SomaDados= dadoUm+dadoDois
        
        if SomaDados == (2, 3, 12):
            RespostaSimNao = str(input('Você já perdeu?! Quer jogar de novo??? '))
            RespostaSimNao = RespostaSimNao.lower()
            
        elif SomaDados == (7, 11):
            RespostaSimNao = str(input('Você venceu! Não quer tentar a sorte de novo? '))
            RespostaSimNao = RespostaSimNao.lower()
        else:
            jogadaUm==SomaDados
            


        
        

    print ('Esperamos que tenha gostado de jogar!!!')
jogo()




   