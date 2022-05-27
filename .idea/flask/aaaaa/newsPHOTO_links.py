import requests
from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent
links=[]
gg=[]
d=0
#ССЫЛКИ
w=[]
z=[]
def get_html(url):
    result = requests.get(url)
    return result.text

html=get_html("https://physics.itmo.ru")
soup=BeautifulSoup(html, "lxml")
for link in soup.find_all('a'):
    #print(link.get('href'))
    try:
        w+=link.get('href')
    except:
        continue

    #if 'news' in str(''.join(c).split('ru')[i]):
w=''.join(w)
w=w[w.find("/ru/news/"):w.find("/ru/news/")+1237]
w=w.split('/ru/n')
for i in range(len(w)):
    if 'https://' not in w[i] and len(w[i])>4:
        #print(c[i])
        z.append(w[i])
for i in range(len(z)):
    z[i]='/ru/n'+z[i]
    ####################print(z[i])
#КОНЕЦ ССЫЛОК
#ПОИСК КАРТИНОК
html_doc = "https://physics.itmo.ru/ru/news"
url = "https://physics.itmo.ru/"

a0 = UserAgent().chrome
page1 = requests.get(html_doc, headers={'User-Agent': a0})
soup = BeautifulSoup(page1.text, "html.parser")

picture = list = []

a = soup.find_all('img')
soup = str(a)
# print(a)
i = 0


def src(i):
    b = ""
    for h in range(3):
        b = b + soup[i]
        i += 1
    return b


while i <= len(soup) - 10:
    url = ""

    # +5
    if src(i) == "src":
        i += 5
        while soup[i] != " ":
            url = url + soup[i]
            i += 1
        url = url[:-4]

        url = "https://physics.itmo.ru/" + url
        picture.append(url)
        i += 1
    else:
        i += 1
i = 0

picture20 = list = []


def ch(i, j):
    a = picture[i]
    b = ""
    for h in range(3):
        b = b + picture[i][j]
        j += 1
    return b


for i in range(len(picture)):
    a = picture[i]
    j = 0
    for j in range(len(a) - 3):
        if ch(i, j) == "800":
            picture20.append(a)
            break

#print(picture)
#for i in range(len(picture20)):
    ##############print(picture20[i], i)
#КОНЕЦ ПОИСКА КАРТИНОК ///////////////////////////////////////////////////////////
FIND = "<nppcc"
"""with open("NewPhystech_OLD.html", 'r+') as f1, open("NewPhystec.html", 'w+') as f2:
    x=f1.readlines()
    for line in x:
            if FIND in line:
                f2.write('			    <a href="https://physics.itmo.ru'+str(z[d])+'">'+"\n"+'                   <img src="'+picture20[d]+'" height="350"></a></li>'+"\n")
                d+=1
            else:

                f2.write(line)

    x=f2.readlines()

print(x)
"""
