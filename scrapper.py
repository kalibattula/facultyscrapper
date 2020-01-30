import requests
from bs4 import BeautifulSoup
import pandas as pd

html_text = requests.get('https://www.albany.edu/ceas/faculty-and-staff-cs')
soup = BeautifulSoup(html_text.text,'html.parser')

faculty_dict = {"name":[],"Designation":[],"email":[]}
content = soup.find_all(class_='content')
# print(type(content[2].find_all('p')[5].get_text()))
ptags = content[2].find_all('p')
atags = content[2].find_all('a',hreflang='en')
# emailtags = content[2].find_all('p').find('a')
# print(atags)

for i in ptags:
    # print(i.get_text())
    if i.get_text().isspace():
        continue
    # print(i.get_text())
    else:
        a = i.find('a',recursive=False)
        if a != None:
            faculty_dict['email'].append(a.get_text())

for i in atags:
    faculty_dict['name'].append(i.get_text())

for i in ptags:
    if (i.get_text().isalpha()) or (' ' in i.get_text() and ('518' not in i.get_text())):
        faculty_dict['Designation'].append(i.get_text())


df = pd.DataFrame(faculty_dict)
df.to_excel('faculty1.xlsx',index=False)


