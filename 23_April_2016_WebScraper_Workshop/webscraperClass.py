# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:13:56 2016

@author: Almazi
"""

import requests
from bs4 import BeautifulSoup 



class DailyStarParser:
    
    def __init__(self):
        page = requests.get('http://thedailystar.net') #importing request and getting the page we want to scrap data from

        self.soup = BeautifulSoup(page.text, "lxml") #To get rid of error use BeautifulSoup([your markup], "lxml")
#lxml is underline html engine to parse specially for all system as it may vary in other system
    def headlinecrap(self):
        headline1 = self.soup.find_all('h1')
        headline2 = self.soup.find_all('h2')
        headline3 = self.soup.find_all('h3')
        headline4 = self.soup.find_all('h4')
        headline5 = self.soup.find_all('h5')
        headline6 = self.soup.find_all('h6')
        all_headline = headline1 + headline2 + headline3 + headline4 + headline5 + headline6
        
        headLineList = []
        
        for all_h in all_headline:
             headLineList.append(all_h.text)
        return headLineList
    
    def categorycrap(self):
        ul = self.soup.find('ul', {'class':'menu'})
        all_a = ul.find_all('a')
        
        all_categories = [category.text for category in all_a]
        
        '''for anchor in all_a:
            all_categories.append(anchor.text)'''
        
        
        all_categories = [category for category in all_categories if not category == ""]
        #first category is the return value
        '''same as the list comprehension above 
        for category in all_categories:
            if category == "":
                all_categories.remove(category)'''
                
        all_categories.sort() #sorted fron A to Z depending on ASCI serial
        return all_categories
    

parser = DailyStarParser()
print(parser.categorycrap())
print(parser.headlinecrap())

