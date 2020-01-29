# -*- coding: utf-8 -*-

from botSpecialist import botSpecialist

class botGeneral:
    def __init__(self):
        pass
    
    def repond(self,q):
        return 'bitch'

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
            