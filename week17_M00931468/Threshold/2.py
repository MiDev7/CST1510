import requests
from bs4 import BeautifulSoup
 
URL = "https://www.earningswhispers.com/stocks/ATVI"

response = requests.get(URL)
soup = BeautifulSoup(response.content,'html.parser')

consensus =  soup.find('div', id='consensus').text
timebox= soup.find('div', id='datebox')
day = timebox.find('div', class_='boxhead').text
date = timebox.find('div', class_='mainitem').text
time = timebox.find('div', id='earningstime').text
print(soup.find('div', id='compname').text)
print(f"{consensus}\n{day} {date} {time}")