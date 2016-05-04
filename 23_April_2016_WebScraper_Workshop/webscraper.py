# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:13:56 2016

@author: Almazi
"""

import requests
from bs4 import BeautifulSoup 

page = requests.get('http://thedailystar.net') #importing request and getting the page we want to scrap data from

soup = BeautifulSoup(page.text, "lxml") #To get rid of error use BeautifulSoup([your markup], "lxml")
#lxml is underline html engine to parse specially for all system as it may vary in other system
'''headline1 = soup.find_all('h1')
headline2 = soup.find_all('h2')
headline3 = soup.find_all('h3')
headline4 = soup.find_all('h4')
headline5 = soup.find_all('h5')
headline6 = soup.find_all('h6')
all_headline = headline1 + headline2 + headline3 + headline4 + headline5 + headline6

totalHeadlines = len(all_headline)

print("Total news today: {0} " .format(totalHeadlines)) #{0} means format list er 0th element, jodi more than one element print korte chai tahole 0, 1, 2 use korte pari
for all_h in all_headline:
    print(all_h.text)
 '''
#print(" ") #for new line
#all_p = soup.find_all('p')[0].text #taking the body text of that headline

#print(all_p)
ul = soup.find('ul', {'class':'menu'})
all_a = ul.find_all('a')

all_categories = []

for anchor in all_a:
    all_categories.append(anchor.text)



all_categories.remove("") #removing the blank elements in list
all_categories.remove("")
all_categories.sort() #sorted fron A to Z depending on ASCI serial
#print(all_categories)

def headlinecrap(input):
    headline1 = soup.find_all('h1')
    headline2 = soup.find_all('h2')
    headline3 = soup.find_all('h3')
    headline4 = soup.find_all('h4')
    headline5 = soup.find_all('h5')
    headline6 = soup.find_all('h6')
    all_headline = headline1 + headline2 + headline3 + headline4 + headline5 + headline6
    
    headLineList = []
    
    for all_h in all_headline:
         headLineList.append(all_h.text)
    return headLineList

def categorycrap(input):
    ul = soup.find('ul', {'class':'menu'})
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


page = requests.get('http://thedailystar.net') #importing request and getting the page we want to scrap data from

Soup = BeautifulSoup(page.text, "lxml")


print("Headline list: ",headlinecrap(soup))
print("Category list: ",categorycrap(soup))


