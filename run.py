import requests,csv
from bs4 import BeautifulSoup
from datetime import datetime
'''
Requests data from the olg lottery to produce 649 winning numbers which are then parsed and put into a csv file 
with the date of the draw

'''
url = "https://lottery.olg.ca/en-ca/winning-numbers/lotto-649/winning-numbers"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

soup.prettify()

winning_nums_html = soup.find_all(class_="winning-numbers-number")
date_of_draw = soup.find(class_='selected-date').text

numbers_sfn = []
for nums in winning_nums_html:
        numbers_sfn.append(nums.text)

dateToday = str(datetime.now().date())
fileName = "649-numbers-"+ dateToday

myFile = open(fileName, 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerow([date_of_draw, numbers_sfn[0], numbers_sfn[1],numbers_sfn[2],numbers_sfn[3],numbers_sfn[4],numbers_sfn[5],numbers_sfn[6]])