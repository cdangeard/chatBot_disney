# -*- coding: utf-8 -*-

from classes.botSpecialist import botSpecialist
from classes.botGeneral import botGeneral

class disneyChatBot:
    
    def __init__(self):
        self.botSpecialist = botSpecialist()
        self.botGeneral = botGeneral()
        
    def repond(self, question):
        reponseSpe = self.botSpecialist.repond(question)
        if reponseSpe:
            return reponseSpe
        else:
            return self.botGeneral.repond(question)
            