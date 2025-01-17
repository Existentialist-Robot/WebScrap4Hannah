# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:34:13 2020

@author: eredm
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


page = requests.get("https://www.ualberta.ca/computing-science/faculty-and-staff/faculty")

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())


card = soup.find(id="card")

card_items = card.find_all(class_="card-container")

this_person = card_items[0]

print(this_person.prettify())

period = this_person.find(class_="period-name").get_text()
print(period)

# period_tags = this_person.select(".tombstone-container .period-name")
# periods = [pt.get_text() for pt in period_tags]
# periods

# short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]

# weather = pd.DataFrame({
#     "period": periods,
#     "short_desc": short_descs,
#     "temp": temps,
#     "desc":descs
# })
# weather

import requests
from bs4 import BeautifulSoup
import pandas as pd

# page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
page = requests.get("https://www.ualberta.ca/computing-science/faculty-and-staff/faculty")

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

soup.select("tr")[1].get_text()

card = soup.find("tr")

card_tags = soup.select("td")
# card_items.find_all("td")


email= [email.get_text() for email in card_tags]

def hasNumbers(inputString):
     return any(char.isdigit() for char in inputString)

def removeNonAlpha(inputString):
    temp = ''
    for char in inputString:
        if char.isalpha():
            temp += char
    return temp

real_emails = []
for x in range(len(email)):
    if x % 4 == 0:
        temp = email[x-1]
        if hasNumbers(temp) == True:
           removeNonAlpha(temp) 
        else:    
            real_emails.append(temp)

with open("C:\Users\eredm\webscraping", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in real_emails:
            writer.writerow(line)