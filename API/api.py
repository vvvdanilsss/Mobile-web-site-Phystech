
!pip install lxml
!pip install requests
!pip install beautifulsoup4
!pip install fake_useragent

from bs4 import BeautifulSoup
from requests import get
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
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

while i <= len(soup)-10:
  url = ""

  # +5
  if src(i) == "src":
    i += 5
    while soup[i] != " ":
      url = url + soup[i]
      i += 1  
    url = url[:-4]

    url = "https://physics.itmo.ru/"+url
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
  for j in range(len(a)-3):
    if ch(i, j) == "800":
      picture20.append(a)
      break
      

  

# print(picture)
print(picture20)
