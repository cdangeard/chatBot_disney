# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import pickle


class DisneyLand_links(object):
    def __init__(self):
        self.domain = 'https://www.disneylandparis.com/fr-fr/faq'
        self.url = self.domain + '/parcs-a-theme/'    
    def getData(self):
        html = requests.get(self.url).text
        self.soup = BeautifulSoup(html, 'lxml')   
    def parseList(self):
        listFAQ = self.soup.find('div', {'class': 'topics-list help-listing'})
        links = []        
        for i in listFAQ.find_all('a', {'class': 'help-link-container'}, limit= 77):
            link = i.get('href')
            links.append(link)
        return links

def DisneyLand(url):
    html = requests.get(url).text
    data = BeautifulSoup(html, 'lxml') 
    faq = {}
    faq['question'] = data.select_one('div.question > div:nth-of-type(2)').text
    faq['reponse'] = data.select_one('div.answer > div:nth-of-type(2)').text
    return faq

def cleanHTML(data):
    props = ['\xa0', '\n']
    for p in props:
        data = data.replace(p, ' ')
    return data
    
dl_a = DisneyLand_links()
dl_a.getData()
links = dl_a.parseList()
del links[10]

FAQ = []
for i in links :
    faq = DisneyLand(i)
    faq['reponse'] = cleanHTML(faq['reponse'])
    FAQ.append(faq)

with open('faq.pkl', 'wb') as f:
    pickle.dump(FAQ, f)