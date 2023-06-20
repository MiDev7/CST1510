import requests
from bs4 import BeautifulSoup
from art import tprint

URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

container_details= soup.find_all('div',class_="caption")

with open("/home/midev/Desktop/Python/CST1510/week17_M00931468/Threshold/products.txt","w") as file:
    file.write("PRODUCTS\n")
    for index,details in enumerate(container_details):
        name = details.find('a').text.replace('...','')
        price = details.find('h4', class_='price').text
        file.write(f"{index}. {name}, {price}\n")
    

