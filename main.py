import requests
from bs4 import BeautifulSoup
url='https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
r=requests.get(url)
# print(r)

soup=BeautifulSoup(r.text)
# print(soup)

names=soup.find_all('a',class_="title")
# for i in names:
#     print(i.text)


print("reviews")
reveiw=soup.find_all('p',class_="review-count")
price=soup.find_all('h4',class_="float-end price card-title pull-right")
# for i in reveiw:
#     print(i.text)
for i in names:
    for j in reveiw:
        for k in price:
            print(i.text,"  ",j.text,"  ",k.text)
