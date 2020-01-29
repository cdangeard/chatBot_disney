# -*- coding: utf-8 -*-
import spacy
import pandas as pd
import numpy as np
from random import sample 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

def buildVectorizer():
    sw = stopwords.words('french')
    sw += ['être', 'avoir']
    return TfidfVectorizer(lowercase=True, stop_words = sw,
                            ngram_range=(1, 1),
                            use_idf=True, smooth_idf=True, # idf lissé
                            sublinear_tf=False, norm='l2')


class botSpecialist:
    
    def __init__(self, dialogueFilename='train_data.csv', seuil = 0.5, randomSeuil = 0.01):
        self.vectorizer = buildVectorizer()
        self.nlp = spacy.load("fr_core_news_sm")
        self.stemmer = SnowballStemmer('french')
        self.seuil = seuil
        self.randomSeuil = randomSeuil
        
        self.base = pd.read_csv(dialogueFilename)
        self.base['lemmas_rep'] = self.base["reponse"].apply(self.lemmatise_text)
        self.base['lemmas_quest'] = self.base["question"].apply(self.lemmatise_text)
        
        self.vectorizedBase = self.vectorizer.fit_transform(
                pd.concat([self.base["lemmas_quest"].apply(self.stem_text) ,
                           self.base["lemmas_rep"].apply(self.stem_text)]))
       
    def lemmatise_text(self, text):
        tweet_nlp = self.nlp(text)
        l = [token.lemma_ for token in tweet_nlp ]
        return (" ".join(l)).replace(" \n","")

    def stem_text(self, text):
        words = word_tokenize(text)
        l = [self.stemmer.stem(token) for token in words]
        return " ".join(l)
        
    def repond(self, question):
        query_corpus_sim = self.rankReponses(question)
        return self.chooseReponse(query_corpus_sim)


    def chooseReponse(self, query_corpus_sim):
        bestSim = np.max(query_corpus_sim)
        if bestSim < self.seuil:
            return ''
        else:
            validIndexes = [ind for ind in range(len(query_corpus_sim))\
                            if query_corpus_sim[ind]>bestSim-self.randomSeuil]
            idchosenOne = sample(validIndexes,1)[0]
        if(idchosenOne >= 144):
             return self.base["reponse"][idchosenOne-144]
        else:
             return self.base["reponse"][idchosenOne]
            
        
    def rankReponses(self, question):
        query = [self.stem_text(self.lemmatise_text(question))]
        query_vector = self.vectorizer.transform(query)
        query_corpus_sim = np.squeeze(cosine_similarity(
                self.vectorizedBase, query_vector))
        return query_corpus_sim