import requests
from bs4 import BeautifulSoup
import time

dir = '/home/midev/Desktop/Python/CST1510/week17_M00931468/Typical/'
ticks = []
with open(f"{dir}ticks.csv", 'r') as file:
    lines = file.readlines()
    for line in lines:
        ticks.append(line.strip().replace('\ufeff',''))

delay = time.sleep(3)
def stocks_scrape(index,extension):
    delay
    try:
        URL = f"https://www.earningswhispers.com/stocks/{extension}"
        response = requests.get(URL)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,'html.parser')

            consensus =  soup.find('div', id='consensus').text.replace('Consensus:','').strip()
            timebox= soup.find('div', id='datebox')
            day = timebox.find('div', class_='boxhead').text
            date = timebox.find('div', class_='mainitem').text
            time = timebox.find('div', id='earningstime').text
            company_name = soup.find('div', id='compname').text

            with open(f"{dir}stocks_tuple.csv","a") as file:
                file.write(f"\"{index + 1}\",\"{company_name}\",\"{consensus}\",\"{day} {date}\",\"{time}\"\n")
            
            print(company_name)
    except:
        pass


if __name__ == "__main__":

    with open(f"{dir}stocks.csv","a") as file:
        file.write(f"ID,COMPANY NAME,CONSENSUS,DATE\n")
    for index,tick in enumerate(ticks):
        stocks_scrape(index,tick)
