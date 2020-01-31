# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 00:26:01 2020

@author: Drimer
"""
from classes.disneyBot import disneyChatBot

bot = disneyChatBot()
print('Bonjour')
while True:
    msg = input()
    if msg == 'quit':
        print('bye')
        break
    else:
        print(bot.repond(msg))