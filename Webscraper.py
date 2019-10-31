import urllib
import bs4
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


page_url = 'https://kurser.lth.se/lot/?val=program&prog=BME'

# Parser
uClient = uReq(page_url)
page_soup = soup(uClient.read(), 'html.parser')
uClient.close()



for table in page_soup.find_all('table', class_="CourseListView border hover lighter_table_head zebra"):
    for container in table.find_all('tr'):

        course_code = container.find('a').string
        course_title = container.find('td', width='250')
        print(course_code)
        print(course_title)

        points = container.find_all('td', class_="mitt")
        for point in points:
            print(point.text)

        lps = container.find_all('span', class_="ttinfo")
        for lp in lps:
            print(lp.strong.text)

