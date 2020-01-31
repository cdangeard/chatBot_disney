# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 00:26:01 2020

@author: Drimer
"""
from classes.disneyBot import disneyChatBot


### Fonction qui execute en boucle des appels au chatbot
#simulant une conversation avec lui.
def chatbot():
    bot = disneyChatBot()
    print('Bonjour')
    while True:
        msg = input()
        #condition d'arret
        if msg == 'quit':
            print('bye')
            break
        else:
            print(bot.repond(msg))

if __name__ == '__main__':
    chatbot()