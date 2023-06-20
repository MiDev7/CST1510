import requests
from bs4 import BeautifulSoup

class Stock:
    def __init__(self,index : int,consensus : str, day : str , date : str, time : str, company_name : str):
        self.__index = index
        self.__consensus = consensus
        self.__day = day
        self.__date = date
        self.__time = time
        self.__company_name = company_name

    def get_consensus(self):
        return self.__consensus
    
    def get_day(self):
        return self.__day
    
    def get_date(self):
        return self.__date
    
    def get_time(self):
        return self.__time
    
    def get_company_name(self):
        return self.__company_name
    
    def __str__(self) -> str:
        return f"{self.__index}. {self.__company_name} Consensus: {self.__consensus} Date: {self.__day} {self.__date} {self.__time}\n"
        
        

class Scrape:
    def __init__(self, url, ticks : list):
        self.__url = url
        self.__result = []
        self.__ticks = ticks


    def scrape(self):
        for index ,tick in enumerate(self.__ticks):       
            try:
                response = requests.get(f"{self.__url}/{tick}")
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content,'html.parser')

                    consensus =  soup.find('div', id='consensus').text.replace('Consensus:','').strip()
                    timebox= soup.find('div', id='datebox')
                    day = timebox.find('div', class_='boxhead').text
                    date = timebox.find('div', class_='mainitem').text
                    time = timebox.find('div', id='earningstime').text
                    company_name = soup.find('div', id='compname').text
                    temp = Stock(index, consensus,day, date, time, company_name)
                    self.__result.append(temp)
                
                    print(company_name)

            except:
                pass

    def display_each_detail(self):
        for item in self.__result:
            print(item)

if __name__ == "__main__":
    dir = '/home/midev/Desktop/Python/CST1510/week17_M00931468/Typical/'
    ticks = []
    with open(f"{dir}ticks.csv", 'r') as file:
        lines = file.readlines()
        for line in lines:
            ticks.append(line.strip().replace('\ufeff',''))

    scrape = Scrape("https://www.earningswhispers.com/stocks/",ticks)
    scrape.scrape()
    scrape.display_each_detail()