# -*- coding: utf-8 -*-

from botSpecialist import botSpecialist

class classifier:
    def __init__(self):
        pass
    
    def is_myJob(self,q):
        return True

class disneyChatBot:
    
    def __init__(self):
        self.classifier = classifier()
        self.botSpecialist = botSpecialist()
        self.botGeneral = None
        
    def repond(self, question):
        if self.classifier.is_myJob(question):
            return self.botSpecialist.repond(question)
        else:
            return self.botGeneral.repond(question)
            