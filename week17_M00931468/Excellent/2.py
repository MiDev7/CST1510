import requests
from bs4 import BeautifulSoup
from art import tprint

class Product:
    def __init__(self,index : int, name : str,price : str):
        self.__index = index
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price

    def __str__(self) -> str:
        return f"{self.__index}. Name: {self.__name}, Price: {self.__price} "

class Scrape: 
    def __init__(self, url : str):
        self.__url = url
        self.__result = []

    def scrape(self):
        response = requests.get(self.__url)
        soup = BeautifulSoup(response.content, 'html.parser')

        container_details= soup.find_all('div',class_="caption")
        for index,details in enumerate(container_details):
                name = details.find('a').text.replace('...','')
                price = details.find('h4', class_='price').text
                temp = Product(index+1,name,price)
                self.__result.append(temp)

    def display_each_product(self):
        for item in self.__result:
            print(item)

if __name__ == "__main__":
    tprint("Products")
    scrape = Scrape("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
    scrape.scrape()
    scrape.display_each_product()