# -*- coding: utf-8 -*-
"""
Updated on Thurs May 5, 2016
Features: Takes input to see latest, any number or announcements according to your wish
Edited: Almazi
"""

import requests #handles web requests
from bs4 import BeautifulSoup #formats the web properties for normal human understanding

def notice_scraper(from_n=0, upto=None):

    dates = []
    notices = []
    for total_notice in range(0,from_n,12):
        url = "http://www.northsouth.edu/nsu-announcements/?anaunc_start={0}".format(total_notice) #Here we will change the url as our notice webpage contains 12 notices per page so if we ask for more/less than 12 notice to see this {0} will be replaced with every 12th integer as its the structure of the pages URL on site
        r = requests.get(url)
        if r.status_code / 100 == 2: #No idea what staus_code does, but will read
            soup = BeautifulSoup(r.text, "lxml")
            h3_finder = [notice_h3.find('a') for notice_h3 in soup.find('div', {'id': 'nsuannouncement'}).find_all('h3')] #it will find all H3 tags inside the div id: nsuannouncement and only return the 'a' parts
            date_finder = [notice_date.get_text().strip()  for notice_date in soup.find('div', {'id': 'nsuannouncement'}).find_all('div', {'id': 'anno-date'})]
            #I couldnt fetch the date data along with H3 data so had to declare one more list comprehension

            for notice, dates in zip(h3_finder, date_finder): #we use zip to use more than one variable and list in same loop

                notices.append({
                    'date' : dates,
                    'title' : notice.text.strip(),
                    'url' : notice.get('href') if notice.get('href')[:7] == "http://" else "http://www.northsouth.edu/" + notice.get('href')}) #here simply checking the http:// or http://www. as prefix of the url and fetching the rest pasrt from the data

    return notices


def show_announcement(n=0):
    all_notice = notice_scraper(from_n=n, upto=n) #calling the function and saving the data
    for printing in range(0,number_of_announcement): #Here I am showing exactly the number for notice you wanted to see.

        print("#",printing+1, ":- Date : ",all_notice[printing]['date'].strip())
        #I couldnt find a way to put month and day on same line. Need help/time
        print("Notice: ",all_notice[printing]['title'])
        print("URL: ",all_notice[printing]['url'])




number_of_announcement = int(input("How many announcement you want to see? : ")) #Taking input as your wish
while number_of_announcement > 82 * 12 or number_of_announcement < 1 :
    number_of_announcement = int(input("Input is too big or too small, better to choose from 1, in 900: "))

show_announcement(number_of_announcement) #calling function

