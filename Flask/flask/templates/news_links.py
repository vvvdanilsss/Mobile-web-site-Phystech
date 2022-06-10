import requests
from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent

links = []
gg = []
d = 0
w = 14


def get_html(url):
    result = requests.get(url)
    return result.text


html = get_html("https://physics.itmo.ru/ru/news")

d1 = 'col-md-6'
d2 = 'col-md-3'


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    # в строчке ниже меняешь d1 и d2///////////////////////////////
    g = soup.find_all("div", class_=d1)
    soup = BeautifulSoup(str(g), "lxml")
    g = soup.find_all('a')
    url_pattern = r'/ru[\S]+'
    urls = list(set(re.findall(url_pattern, str(g))))
    for i in range(len(urls)):
        c = 'https://physics.itmo.ru' + str(urls[i][:-2])
        links.append(c)
        # print('https://physics.itmo.ru'+urls[i])
        # print(links[i])


def main():
    get_data(html)


if __name__ == "__main__":
    main()

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

# -*- coding: utf-8 -*-
"""api.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1Em_Wfv33C4EaHw2RrBwynwLNYHSXcD-M
"""

import requests
from urllib.request import urlopen
from lxml import html


def kod(link):
    url = link
    headers = {'Content-Type': 'text/html', }
    response = requests.get(url, headers=headers)
    tree = html.fromstring(response.content)
    return tree


def parsing(link):
    url = link
    headers = {'Content-Type': 'text/html', }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def poisk(c):
    n = ""
    i = 24
    a = str(re.search("field field--name", c))
    if a != "None":
        while a[i] != ",":
            n += a[i]
            i += 1
        n = int(n)
        return n
    else:
        return "1"


def udalenie(c, i):
    c = c[:poisk(c)] + "g" + c[poisk(c) + 1:]
    return c


def dobavlenie(soup):
    i = poisk(soup)
    while soup[i] != ">":
        i += 1
    i += 1
    c = ""
    while soup[i] != "<":
        c += soup[i]
        i += 1
    # print(c)
    return c


def links(soup):
    n = ""
    i = poisk(soup) - 35
    while soup[i] != "=":
        i -= 1
    i += 2
    while soup[i] != ">":
        n += soup[i]
        i += 1
    for i in range(2):
        n[:len(n) - 1]
    return n


soup = str(parsing("https://physics.itmo.ru/ru/media/press"))
# tree = kod("https://physics.itmo.ru/ru/media/press")
# a = tree.xpath('//div[@class="field field--name"]/text()')
# a = str(a[0])

kods = []

# poisk(soup) != "1"


smi_about = []
smi_links = []

for i in range(17):
    c = ""
    smi_links.append(links(soup))
    while dobavlenie(soup) != '':
        # kods.append(poisk(soup))
        # kods.append(dobavlenie(soup))
        c += "<br><br>" + dobavlenie(soup)
        soup = udalenie(soup, poisk(soup))
    kods.append(c)
    soup = udalenie(soup, poisk(soup))

smi_about = kods

tree = kod("https://physics.itmo.ru/ru")

####### Главная страница #######

# Get element using XPath

# Новости

opisanie_news = tree.xpath('//div[@class="node--title"]/text()')
photo_news = tree.xpath('//img[@class="img-responsive"]/@src')
# //img[@class='photo-large']/@src

# print(opisanie_news)
# print(photo_news)


# надо писать окончательный путь
# Семинары
tree = kod("https://physics.itmo.ru/ru/seminars")
semianrs_photo = tree.xpath('//img[@class="img-responsive"]/@src')
semianars_topic1 = tree.xpath('//div[@class="seminar-type-value"]/text()')
seminars_names_speakers = tree.xpath('//div[@class="external-speaker-wrapper"]/text()')
semianars_topic2 = tree.xpath('//div[@class="speaker-talk-name"]/text()')
semianars_time_date = tree.xpath('//div[@class="dte"]/text()')
semianars_time_time = tree.xpath('//div[@class="tme"]/text()')
seminars_href = tree.xpath('//div[@class="views-row"]/a/@href')

# сделать функцию tree.path...


###### Сотрудники ######

tree = kod("https://physics.itmo.ru/ru/people")
sotrudniki_photo = tree.xpath('//img[@class="img-responsive"]/@src')
sotrudniki_name1 = tree.xpath(
    '//div[@class="field field--name-name field--type-string field--label-hidden field--item"]/text()')
sotrudniki_name2 = tree.xpath(
    '//div[@class="field field--name-second-name field--type-string field--label-hidden field--item"]/text()')
sotrudniki_about = tree.xpath(
    '//div[@class="field field--name-main-position field--type-entity-reference field--label-hidden field--item"]/text()') * 2
sotrudniki_about_links = tree.xpath('//div[@class="node--wrap"]/@src')
# поискать


###### видео ######

tree = kod("https://physics.itmo.ru/ru/media/video")
videos_video = tree.xpath('//iframe[@width="854"]/@src')
videos_about = tree.xpath(
    '//div[@class="field field--name-name field--type-string field--label-hidden field--item"]/text()')
videos_photo = tree.xpath(
    '//div[@class="video-embed-field-provider-youtube video-embed-field-responsive-video form-group"]/iframe/@src')
videos_picture = []
a = "https://i.ytimg.com/vi_webp/"
c = "/sddefault.webp"
for i in range(len(videos_video)):
    videos_video[i] = str(videos_video[i])
    j = 30
    b = ""
    while videos_video[i][j] != "?":
        b = b + videos_video[i][j]
        j += 1
    videos_picture.append(a + b + c)

###### вакансии ######

# создаётся словарь с названием вакансией и описанием

tree = kod("https://physics.itmo.ru/ru/vacancies")
vacancies_name = tree.xpath('//a[@hreflang="ru"]/text()')
vacancies_topic = tree.xpath('//h3/text()')

####### софт ########
# создать словарь

tree = kod("https://physics.itmo.ru/ru/soft")
soft_name = tree.xpath('//span[@class="field-content"]/text()')
soft_author = tree.xpath('//a[@hreflang="ru"]/text()')
soft_links = tree.xpath('//div[@class="field-content"]/@src')  # не работает

####### сми ########


tree = kod("https://physics.itmo.ru/ru/media/press")
smi_name = tree.xpath(
    '//div[@class="field field--name-type field--type-list-integer field--label-hidden field--item"]/text()')
smi_who = tree.xpath(
    '//div[@class="field field--name-source field--type-entity-reference field--label-hidden field--item"]/text()')
smi_about = tree.xpath(
    '//div[@class="field field--name-name field--type-string field--label-hidden field--item"]/text()')
smi_date = tree.xpath('//time//text()')

###### научные группы #######

tree = kod("https://physics.itmo.ru/ru/research-groups")

group_name = tree.xpath(
    '//div[@class="research-group-group-name"]/text()')  # переделать в str и убрать пробелы и добаввить группа
group_photo = tree.xpath('//img[@class="img-responsive"]/@src')

# надо разделить персоны на группы
group_spisok_name = tree.xpath(
    '//div[@class="field field--name-name field--type-string field--label-hidden field--item"]/text()')
group_spisok_surname = tree.xpath(
    '//div[@class="field field--name-second-name field--type-string field--label-hidden field--item"]/text()')
group_spisok_rank = tree.xpath(
    '//div[@class="field field--name-main-position field--type-entity-reference field--label-hidden field--item"]/text()')
# надо сделать описание научной группы


###### публикации ########
# будут только ссылки на доки с публикациями

tree = kod("https://physics.itmo.ru/ru/publications")
publi_links = tree.xpath('//div[@class="export-links"]/span[@class="papers-export-link export-gost"]/a/@href')

###### стажировки школьников летняя практика ######

tree = kod("https://physics.itmo.ru/ru/internship/school/summer")

# добавить форматы
stage_sum_date = tree.xpath(
    '//div[@class="field field--name-internship-date-text field--type-text-long field--label-hidden field--item"]/p/text()')
# летняя практика пройдёт
stage_sum_deadline = tree.xpath(
    '//div[@class="field field--name-internship-date-end-text field--type-text-long field--label-hidden field--item"]/p/span[@class="internship-dates-yellow-date"]/text()')

# подать заявку
stage_sum_podat = tree.xpath(
    '//div[@class="field field--name-internship-date-button field--type-link field--label-hidden field--item"]/a/@href')

stage_sum_about_last_year = tree.xpath(
    '//div[@class="field field--name-internship-project-desc field--type-text-long field--label-hidden field--item"]/p/text()')

# внутри уже есть год
stage_sum_comments = tree.xpath('//div[@class="field-content"]/p/text()')

# добавить команда проекта
stage_sum_team = tree.xpath(
    '//div[@class="field field--name-internship-teams-person-text field--type-string field--label-hidden field--item"]/text()')

stage_sum_img_ruk = tree.xpath('//img[@width="300"]/@src')
stage_sum_name_ruk = tree.xpath(
    '//div[@class="field field--name-name field--type-string field--label-hidden field--item"]/text()')
stage_sum_surname_ruk = tree.xpath(
    '//div[@class="field field--name-second-name field--type-string field--label-hidden field--item"]/text()')

stage_sum_rank = tree.xpath(
    '//div[@class="field field--name-main-position field--type-entity-reference field--label-hidden field--item"]/text()')

########## стажировки школьников годовая практика #########

tree = kod("https://physics.itmo.ru/ru/internship/school/yearly")

stage_year_about_name = tree.xpath(
    '//div[@class="field field--name-internship-project-name field--type-string field--label-hidden field--item"]/text()')
stage_year_about = tree.xpath(
    '//div[@class="field field--name-internship-project-desc field--type-text-long field--label-hidden field--item"]/text()')
stage_year_rank = tree.xpath('//div[@class="field--label"]/text()')
stage_year_uchastniki = tree.xpath(
    '//div[@class="field field--name-internship-teams-person-text field--type-string field--label-above"]/div[@class="field--item"]/text()')
# убрать лишние элементы
stage_year_names = tree.xpath('//div[@class="field--item"]/a/text()')
stage_year_itogi = tree.xpath(
    '//div[@class="field field--name-internship-results field--type-text-long field--label-above"]/div[@class="field--item"]/text()')
stage_year_video = tree.xpath('//iframe[@height="480"]/@src')

# НОВОСТИ
tree = kod("https://physics.itmo.ru/ru/news")
hrefs_news = tree.xpath('//div[@class="col-md-6 views-row"]/a/@href')
hrefs_newsLast = tree.xpath('//div[@class="col-md-6 big-node"]/a/@href')


###### научные группы #######


def im(a, k):
    i = 37
    b = ""
    g = ""
    while a[k][i] != "\n":
        b += a[k][i]
        i += 1
    i = 75
    while a[k][i] != "\n":
        g += a[k][i]
        i += 1
    b = "Группа " + b + " " + g
    return b


a = []
group_names = []
group_name = []  # название группы

tree = kod("https://physics.itmo.ru/ru/research-groups")
a = tree.xpath('//div[@class="research-group-group-name"]/text()')
group_group = tree.xpath(
    '//div[@class="views-field views-field-title"]/span[@class="field-content"]/a[@class="use-ajax"]/div[@class="research-group-group-name"]/text()')
group_links = tree.xpath('//span[@class="field-content"]/a/@href')

for k in range(len(a)):
    group_name.append(im(a, k))

names = []
surnames = []
group_full_names = []  # имя и фамилия персон
group_full_photo = []  # фото персон
rank = []

for i in range(len(group_links)):
    tree = kod("https://physics.itmo.ru/ru/" + group_links[i])
    group_names = tree.xpath(
        '//div[@class="field field--name-name field--type-string field--label-hidden field--item"]/text()')
    group_surnames = tree.xpath(
        '//div[@class="field field--name-second-name field--type-string field--label-hidden field--item"]/text()')
    group_photo = tree.xpath(
        '//div[@class="field field--name-photo field--type-image field--label-hidden field--item"]/img/@src')
    names.append(group_names)
    surnames.append(group_surnames)
    rank.append(group_photo)

for i in range(len(names)):
    g = []
    h = []
    for j in range(len(names[i])):
        if j == 0:
            g.append(names[i][j] + " " + surnames[i][j] + " (Руководитель группы)")
        else:
            g.append(names[i][j] + " " + surnames[i][j])
        h.append("https://physics.itmo.ru/" + rank[i][j])
    group_full_names.append(g)
    group_full_photo.append(h)

####### аспирантура #########
tree = kod("https://physics.itmo.ru/ru/admission/phd")

asp_kod_program = tree.xpath(
    '//div[@class="field field--name-name field--type-string field--label-hidden field--item"]/text()')
asp_names_program = tree.xpath(
    '//div[@class="field field--name-description field--type-text-long field--label-hidden field--item"]/text()')
asp_date = tree.xpath(
    '//div[@class="field field--name-adm-phd-date field--type-datetime field--label-hidden field--item"]/time/text()')
asp_date_about = tree.xpath(
    '//div[@class="field field--name-adm-phd-date-text field--type-string field--label-hidden field--item"]/text()')

asp_napravlenia = tree.xpath('//div[@class="node--wrap"]/h2[@class="node-title"]/span/text()')
asp_napravlenia_about = tree.xpath(
    '//div[@class="field field--name-short-description field--type-text-long field--label-hidden field--item"]/p/text()')

asp_kontact_photo = tree.xpath(
    '//div[@class="field field--name-photo field--type-image field--label-hidden field--item"]/img/@src')
asp_kontact_name = tree.xpath('//div[@class="personality-admission-name"]/text()')
asp_kontact_rank = tree.xpath('//div[@class="personality-admission-position"]/text()')
asp_kontact_pochta = tree.xpath('//div[@class="personality-admission-email"]/text()')
asp_kontact_number = tree.xpath('//div[@class="personality-admission-phone"]/a/text()')

# tree.xpath('//div[@class=""]/')

# //ul[@class='facetOptions']/li/a[@role='checkbox']/@href


########## бакалавриат #######

tree = kod("https://physics.itmo.ru/ru/admission/bachelor")

bac_budj_mest = tree.xpath(
    '//div[@class="field field--name-budget-places field--type-integer field--label-above"]/div[@class="field--item"]/text()')
bac_kontr_mest = tree.xpath(
    '//div[@class="field field--name-paid-places field--type-integer field--label-above"]/div[@class="field--item"]/text()')
bac_prohod = tree.xpath(
    '//div[@class="field field--name-exam-results field--type-integer field--label-above"]/div[@class="field--item"]/text()')

####### магистратура #########

tree = kod("https://physics.itmo.ru/ru/admission/master/advanced-quantum-and-nanophotonic-systems")
asp1_budjet = tree.xpath(
    '//div[@class="admission-master-in-a-glance-column-2"]/div[@class="field field--name-adm-master-budget-places field--type-integer field--label-above"]/div[@class="field--item"]/text()')
asp1_contract = tree.xpath(
    '//div[@class="field field--name-adm-master-paid-places field--type-integer field--label-above"]/div[@class="field--item"]/text()')
asp1_vstup = tree.xpath(
    '//div[@class="field field--name-adm-master-entrance-exams field--type-link field--label-above"]/div[@class="field--items"]/div[@class="field--item"]/a/text()')

tree = kod("https://physics.itmo.ru/ru/admission/master/physics-of-radio-frequency-technologies")
asp2_budjet = tree.xpath(
    '//div[@class="admission-master-in-a-glance-column-2"]/div[@class="field field--name-adm-master-budget-places field--type-integer field--label-above"]/div[@class="field--item"]/text()')
asp2_contract = tree.xpath(
    '//div[@class="field field--name-adm-master-paid-places field--type-integer field--label-above"]/div[@class="field--item"]/text()')
asp2_vstup = tree.xpath(
    '//div[@class="field field--name-adm-master-entrance-exams field--type-link field--label-above"]/div[@class="field--items"]/div[@class="field--item"]/a/text()')

tree = kod("https://physics.itmo.ru/ru/admission/master/photonics-and-spintronics")
asp3_budjet = tree.xpath(
    '//div[@class="admission-master-in-a-glance-column-2"]/div[@class="field field--name-adm-master-budget-places field--type-integer field--label-above"]/div[@class="field--item"]/text()')
asp3_contract = tree.xpath(
    '//div[@class="field field--name-adm-master-paid-places field--type-integer field--label-above"]/div[@class="field--item"]/text()')
asp3_vstup = tree.xpath(
    '//div[@class="field field--name-adm-master-entrance-exams field--type-link field--label-above"]/div[@class="field--items"]/div[@class="field--item"]/a/text()')

d = 0
# """
# Главная страница
FIND1 = "<linews"
FIND2 = "<lisem"
with open("NewPhystech_OLD.html", 'r+', encoding='utf-8') as f1, open("NewPhystech.html", 'w+', encoding='utf-8') as f2:
    x = f1.readlines()
    for line in x:
        if FIND1 in line:
            if d != 4:
                f2.write('			    <a href="/news' + str(
                    d + 1) + '">' + "\n" + '                <img class="general-photo" src="' + picture20[
                             d] + '">' + "\n" + '                ' + "\n" + '                <h5>' + opisanie_news[
                             d] + '</h5></a></li>' + "\n")
            else:
                f2.write('			    <a href="/news' + str(
                    d + 1) + '">' + "\n" + '                <img class="general-photo" src="' + picture20[
                             d] + '">' + "\n" + '                ' + "\n" + '               <h5>' + opisanie_news[
                             d] + '</h5></a></li>' + "\n")
                d = 0
            d += 1
        if FIND2 in line:
            f2.write('			    <a href="https://physics.itmo.ru' + str(seminars_href[
                                                                                  d - 1]) + '">' + "\n" + '                <img class="general-photo" src="https://physics.itmo.ru/' +
                     semianrs_photo[d - 1] + '">' + "\n" + '                ' + "\n" + '                <h5>' + str(
                semianars_topic2[d - 1]).replace('\n\t\t\t', '') + '</h5></a></li>' + "\n")
            d += 1
        else:

            f2.write(line)
d = 0

# ВИДЕО
FIND = '<livid'
with open("video_OLD.html", 'r+', encoding='utf-8') as f1, open("video.html", 'w+', encoding='utf-8') as f2:
    x = f1.readlines()
    for line in x:
        if FIND in line:
            f2.write('			        <a href="' + str(
                videos_video[d]) + '" >' + "\n" + '					    <img src="' + videos_picture[
                         d] + '" alt="Avatar" style="border-radius:10px; width:320px;">' + "\n" + '				<p>' + str(
                videos_about[d]) + '</p></a></li>' + "\n")
            d += 1
        else:
            f2.write(line)
d = 0

# Сотрудники

FIND = '<listaff2'
d = 0
with open("staff_start.html", 'r+', encoding='utf-8') as f1, open("staff_OLD.html", 'w+', encoding='utf-8') as f2:
    x = f1.readlines()
    for line in x:
        if FIND in line:
            f2.write((
                                 '		<li style="color:black; text-align:center;">' + '\n' + '			<img src="staff_src" alt="Avatar" style="border-radius: 50%;">' + '\n' + '                <p>staff_name</p>' + '\n' + '                <p>staff_about</p>' + '\n' + '        </li>' + '\n') * (
                                 len(sotrudniki_photo) - 5))
        else:
            f2.write(line)

d = 0
c = 0
FIND1 = 'staff_src'
FIND2 = 'staff_name'
FIND3 = 'staff_about'
with open("staff_OLD.html", 'r+', encoding='utf-8') as f1, open("staff.html", 'w+', encoding='utf-8') as f2:
    x = f1.readlines()
    for line in x:
        if c < len(sotrudniki_photo):
            if FIND1 in line:
                f2.write('			<img src="https://physics.itmo.ru/' + str(
                    sotrudniki_photo[d]) + '" alt="Avatar" style="border-radius: 50%;">' + "\n")
                c += 1
                continue
            if FIND2 in line:
                f2.write(
                    '              <p>' + str(sotrudniki_name1[d]) + ' ' + str(sotrudniki_name2[d]) + '</p>' + "\n")
                continue
            if FIND3 in line:
                f2.write('          <p>' + str(sotrudniki_about[d]) + '</p>' + "\n")
                d += 1
            else:
                f2.write(line)
        else:
            f2.write(line)

# НОВОСТИ
d = 0
c = []

FIND = '<p3'
FIND1 = 'Название новости'
for i in range(1, 6):
    d = 0
    c = []
    nwli = 'https://physics.itmo.ru/' + hrefs_news[i - 1]
    tree = kod(str(nwli))
    nwps = tree.xpath(
        '//div[@class="field field--name-body field--type-text-with-summary field--label-hidden field--item"]/p/text()')
    c.append(nwps)
    newssite = 'z_news_' + str(i) + '.html'
    with open("shabnews.html", 'r+', encoding='utf-8') as f1, open(newssite, 'w+', encoding='utf-8') as f2:
        x = f1.readlines()
        for line in x:
            if FIND1 in line:
                f2.write(f'<h1 style="text-align: center;">{opisanie_news[i - 1]}</h1>')
            if FIND in line:
                try:
                    f2.write('<p>' + str(c[0][d]) + '</p>' + '\n')
                    # print(str(c[0][d]))
                    d += 1
                    continue
                except:
                    continue
            else:
                f2.write(line)
                continue
# """
d = 0

FIND1 = 'prohod-b'
FIND2 = 'budj-b'
FIND3 = 'kontr-b'
with open("bacalavriat_OLD.html", 'r+', encoding='utf-8') as f1, open("bacalavriat.html", 'w+', encoding='utf-8') as f2:
    x = f1.readlines()
    for line in x:
        if FIND1 in line:
            f2.write(str(*bac_prohod) + '\n')
            continue
        if FIND2 in line:
            f2.write(str(*bac_budj_mest) + '\n')
            continue
        if FIND3 in line:
            f2.write(str(*bac_kontr_mest) + '\n')
        else:
            f2.write(line)
d = 0

FIND2 = 'budj-b'
FIND3 = 'kontr-b'
with open("magistreSovr_OLD.html", 'r+', encoding='utf-8') as f1, open("magistreSovr.html", 'w+',
                                                                       encoding='utf-8') as f2:
    x = f1.readlines()
    for line in x:
        if FIND2 in line:
            f2.write(str(*asp1_budjet) + '\n')
            continue
        if FIND3 in line:
            f2.write(str(*asp1_contract) + '\n')
        else:
            f2.write(line)
d = 0
FIND2 = 'budj-b'
FIND3 = 'kontr-b'
with open("magistreRad_OLD.html", 'r+', encoding='utf-8') as f1, open("magistreRad.html", 'w+', encoding='utf-8') as f2:
    x = f1.readlines()
    for line in x:
        if FIND2 in line:
            f2.write(str(*bac_budj_mest) + '\n')
            continue
        if FIND3 in line:
            f2.write(str(*bac_kontr_mest) + '\n')
        else:
            f2.write(line)
d = 0
FIND2 = 'budj-b'
FIND3 = 'kontr-b'
with open("magistreFot_OLD.html", 'r+', encoding='utf-8') as f1, open("magistreFot_OLD.html", 'w+',
                                                                      encoding='utf-8') as f2:
    x = f1.readlines()
    for line in x:
        if FIND2 in line:
            f2.write(str(*bac_budj_mest) + '\n')
            continue
        if FIND3 in line:
            f2.write(str(*bac_kontr_mest) + '\n')
        else:
            f2.write(line)
d = 0
c = 0
FIND1 = '<hhh'
FIND2 = '<imggg'
FIND3 = '<pppp'
with open("science-groups_OLD.html", 'r+', encoding='utf-8') as f1, open("science-groups.html", 'w+',
                                                                         encoding='utf-8') as f2:
    x = f1.readlines()
    for line in x:
        if FIND1 in line:
            f2.write('<h2>' + str(group_name[c]) + '</h2>' + '\n')
            continue
        if FIND2 in line:
            f2.write('<img src="' + str(group_full_photo[c][d]) + '>"' + '\n')
            continue
        if FIND3 in line:
            f2.write('<p>' + str(group_full_names[c][d]) + '</p>' + '\n')
            d += 1
            if d == 5:
                c += 1
            continue
        else:
            f2.write(line)
d = 1
FIND = 'qqqq'
with open("vacancy_OLD.html", 'r+', encoding='utf-8') as f1, open("vacancy.html", 'w+', encoding='utf-8') as f2:
    x = f1.readlines()
    for line in x:
        if FIND in line:
            f2.write(str(vacancies_name[d]))
            d += 1
            continue
        else:
            f2.write(line)
d = 0

# hrefs_newsLast[0]
"""
FIND='<li'
with open("smiabobus.html", 'r+', encoding='utf-8') as f1, open(".html", 'w+', encoding='utf-8') as f2:
    x=f1.readlines()
    for line in x:
            if FIND in line:
                f2.write('https://physics.itmo.ru/'+str([d])
                d+=1
            else:
                f2.write(line)
d=0
"""
# Шаблон
"""

FIND='<li'
with open(".html", 'r+', encoding='utf-8') as f1, open(".html", 'w+', encoding='utf-8') as f2:
    x=f1.readlines()
    for line in x:
            if FIND in line:
                f2.write('https://physics.itmo.ru/'+str([d])
                d+=1
            else:
                f2.write(line)
d=0

"""
