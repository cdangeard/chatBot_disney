# -*- coding: utf-8 -*-
import pickle
import spacy


class botSpecialist:
    
    def __init__(self, dialogueFilename='faq.pkl'):
        with open(dialogueFilename, 'rb') as handle:
            self.base = pickle.load(handle)
        self.nlp = spacy.load("fr_core_news_md")

        
    def repond(self, question):
        qdoc = self.nlp(question)
        reponse = None
        simMax = 0
        for paire in self.base:
            sim = qdoc.similarity(self.nlp(paire['question'])) 
            if sim > simMax:
                simMax = sim
                reponse = paire['reponse']
        return reponse
    
    def fit(self):
        pass
    
    def predictTheme(self, question):
        pass
    
    def chooseResponse(self, question):
        pass
    
    def regexResponse(self, question):
        pass