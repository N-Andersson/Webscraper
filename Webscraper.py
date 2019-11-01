import urllib
import bs4
import re
from urllib.request import urlopen as uReq
from urllib.parse import quote
from bs4 import BeautifulSoup as soup


page_url = 'https://kurser.lth.se/lot/?val=program&prog=BME'

# Parser
uClient = uReq(page_url)
page_soup = soup(uClient.read(), 'html.parser')
uClient.close()
filename = "KursutbudBME.csv"
f = open(filename, "w")

print(page_soup.original_encoding)
for table in page_soup.find_all('table', class_="CourseListView border hover lighter_table_head zebra"):
    for container in table.find_all('tr'):


        #Must fix so the a-, and td-tags texts are extracted
        course_code_container = container.find('a')
        try:
            course_code = course_code_container.text
            
        except:
            course_code = "None"
        
        f.write(course_code + ",")
        
        
        course_title_container = container.find('td', width='250')
        try:
            course_title = course_title_container.text.replace(",", "|")
        
        except:
            course_title = "None"
        f.write(course_title + ",")


        points = container.find_all('td', class_="mitt")
        for point in points:
            f.write(point.text.replace(",", ".").replace("\n", "") + ",")
            print(point.text.replace(",", ".") + ",")
        lps = container.find_all('span', class_="ttinfo")
        
        for lp in lps:
            period = lp.find_all('strong')
            f.write(period[0].text + ",")
        f.write("\n")
        

f.close()
print("done")