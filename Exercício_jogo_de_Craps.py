# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:17:57 2020

@author: Pedro Drumond
"""

import random

def jogo()  :
    RespostaSimNao = str(input('Você quer jogar nosso maravilhoso Craps (sim/não)???'))
    RespostaSimNao = RespostaSimNao[0].lower()
    
    while RespostaSimNao == 'sim':
        dadoUm = random.randint(1,6)
        dadoDois = random.randint(1,6)
        SomaDados= dadoUm+dadoDois
        
        if SomaDados == (2, 3, 12):
            print ('Você já perdeu?! Quer jogar de novo???')
        
        

    print ('Esperamos que tenha gostado de jogar!')

print ('testando outra vez')
   