# -*- coding: utf-8 -*-
import tensorflow as tf 
import pickle
import numpy as np
import re


#Bot répondant d'apres un modele préentrainé importé en entree
class botGeneral:
        
    def __init__(self, filenameModel = 'data/last_model.h5', filenameVocab = 'data/vocab.pickle', sizeMaxReponse = 100, temperature = 1.0):
        self.model = tf.keras.models.load_model(filenameModel)
        self.temperature = temperature
        self.sizeMaxReponse = sizeMaxReponse
        #On se sert du vocab pour identifié des caractères à des entiers à
        #l'aide d'une table
        with open(filenameVocab, 'rb') as file:
            vocab = pickle.load(file)
            self.char2idx = {u:i for i, u in enumerate(vocab)}
            self.idx2char = np.array(vocab)
    
    #Une fonction pour mettre en forme le texte et suprimer certains caracteres
    #non adaptés au modèle.
    def pre_process(self, text):
          text = (text.replace("\n-","")
                 .replace("\n",".")
                 .replace("\"" , "")
                 .replace("....","...")
                 .replace("!.","! ")
                 .replace("?.","? ")
                 .replace(":.","")
                 .replace("...",".")
                 .replace("M.","M-")
                 )
          regex = r"(?<=[a-z])(\.\.)(?=[a-zA-Z0-9])"
          text = re.sub(regex , r". " , text)
          regex = r'((\.)(?=[A-Z]))'
          text = re.sub(regex , r". " , text)
          regex = r"(?<=[a-z])(\.)(?=[a-zA-Z0-9])"
          text = re.sub(regex , r" " , text)
          regex = r"(?<=[a-z])(\.\s)(?=[a-z])"
          text = re.sub(regex , r" " , text)
          return text
    
    #fourni la réponse du bot à une requete
    def repond(self, question):
        query = self.pre_process(question)
        return self.genere_phrase(query)
    
    #genere itérativement la réponse du modele caractère par caractère
    #dispose d'une condtion d'arret sur les "finisseurs" de phrase . ! ?
    def genere_phrase(self, start_string):
        input_eval = [self.char2idx[s] for s in start_string]
        input_eval = tf.expand_dims(input_eval, 0)
        # Empty string to store our results
        text_generated = []
        self.model.reset_states()
        
        for i in range(self.sizeMaxReponse):
            predictions = self.model(input_eval)
            # remove the batch dimension
            predictions = tf.squeeze(predictions, 0)

            predictions = predictions / self.temperature
            predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

            # We pass the predicted word as the next input to the model
            # along with the previous hidden state
            input_eval = tf.expand_dims([predicted_id], 0)
    
            text_generated.append(self.idx2char[predicted_id])
            #condtion de fin de pharse (ne prend pas en compte le ... pour le moment)
            if self.idx2char[predicted_id] in ['.','?','!']:
                break
    
        return (''.join(text_generated))
    
