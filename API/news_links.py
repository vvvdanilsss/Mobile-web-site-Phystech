import requests
from bs4 import BeautifulSoup
import re
#626 строчка
links=[]
gg=[]
d=0
def get_html(url):
    result = requests.get(url)
    return result.text

html=get_html("https://physics.itmo.ru/ru/news")

d1='col-md-6'
d2='col-md-3'

def get_data(html):
    soup=BeautifulSoup(html, "lxml")
    #в строчке ниже меняешь d1 и d2///////////////////////////////
    g= soup.find_all("div", class_= d1)
    soup = BeautifulSoup(str(g), "lxml")
    g=soup.find_all('a')
    url_pattern = r'/ru[\S]+'
    urls = list(set(re.findall(url_pattern, str(g))))
    for i in range(len(urls)):
        c='https://physics.itmo.ru'+str(urls[i][:-2])
        links.append(c)
        #print('https://physics.itmo.ru'+urls[i])
        print(links[i])

def main():
    get_data(html)

if __name__ == "__main__":
    main()
FIND = "<nppcc"
with open("NewPhystech_OLD.html", 'r+') as f1, open("NewPhystech.html", 'w+') as f2:
    x=f1.readlines()
    for line in x:
            if FIND in line:
                f2.write('			    <a href="'+str(links[d])+'"></a></li>'+"\n")
                d+=1
            else:

                f2.write(line)

    x=f2.readlines()

print(x)

