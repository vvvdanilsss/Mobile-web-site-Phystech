import requests
from bs4 import BeautifulSoup
import re
#626 строчка
links=[]
gg=[]
def get_html(url):
    result = requests.get(url)
    return result.text

html=get_html("https://physics.itmo.ru/ru/news")

d1='col-md-6'
d2='col-md-3'

def get_data(html):
    soup=BeautifulSoup(html, "lxml")
    #в строчке ниже меняешь d1 и d2///////////////////////////////
    g= soup.find_all("div", class_= d2)
    soup = BeautifulSoup(str(g), "lxml")
    g=soup.find_all('a')
    url_pattern = r'/ru[\S]+'
    urls = list(set(re.findall(url_pattern, str(g))))
    for i in range(len(urls)):
        print('https://physics.itmo.ru'+urls[i])


def main():
    get_data(html)

if __name__ == "__main__":
    main()


