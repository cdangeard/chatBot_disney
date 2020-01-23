# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import os

class DisneyLand(object):
    def __init__(self):
        self.domain = 'https://www.disneylandparis.com/fr-fr/faq'
        self.url = self.domain + '/parcs-a-theme/'    
    def getData(self):
        html = requests.get(self.url).text
        self.soup = BeautifulSoup(html, 'lxml')   
    def parseList(self):
        listQuestion = self.soup.find('div', {'class': 'topics-list help-listing'})
        FAQ = []        
        for i in listQuestion.find_all('article', {'class': 'topic'}, limit= 77):
            faq = {}
            faq['question'] = i.select_one('div.question > div:nth-of-type(2)').text
            faq['reponse'] = i.select_one('div.answer > div:nth-of-type(2)').text
            FAQ.append(faq)
        return FAQ
    def cleanHTML(self, data):
        props = ['\t', '\n', '\r']
        for p in props:
            data = data.replace(p, '')
        return data

    
dl = DisneyLand()
dl.getData()
parsedJson = json.dumps(dl.parseList(), ensure_ascii=False)
print(dl.cleanHTML(parsedJson))