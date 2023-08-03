#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen

url = "https://www.volcanodiscovery.com/earthquakes/bangladesh/largest.html"
web_page = bs4.BeautifulSoup(requests.get(url, {}).text, "lxml") #Extracting HTML of the static webpage
web_page #The HTML code of the page


tables = web_page.find_all(name="script") #With class name
#tables
#len(tables)

result = []
for i in tables:
    for j in i:
        if "var quakesAreSorted=false" in j:
            targetData = j

x = targetData.split("addQuakeToMap")
#print(x)
info = []
for i in x:
    if "GMT: Mag" in i:
        info.append(i)

#print(len(info))

x = info[0].split(",")

date = []
day = []
lat = []
lng = []
year = []
month = []
time = []
mag = []
area = []
country = []
#fn = []
for i in info:
    x = i.split(",")
    y = x[4].split(" ")
    date.append(f"{x[3]}, {y[1]}")
    z = x[3].split(" ")
    day.append(z[1])


    if x[3][1:4] == "Jan": month.append("January")
    elif x[3][1:4] == "Feb": month.append("February")
    elif x[3][1:4] == "Mar": month.append("March")
    elif x[3][1:4] == "Apr": month.append("April")
    elif x[3][1:4] == "May": month.append("May")
    elif x[3][1:4] == "Jun": month.append("June")
    elif x[3][1:4] == "Jul": month.append("July")
    elif x[3][1:4] == "Aug": month.append("August")
    elif x[3][1:4] == "Sep": month.append("September")
    elif x[3][1:4] == "Oct": month.append("October")
    elif x[3][1:4] == "Nov": month.append("November")
    elif x[3][1:4] == "Dec": month.append("December")


    lat.append(x[1])
    lng.append(x[2])
    year.append(y[1])
    time.append(y[2])
    mag.append(y[-1])
    #fn.append((x[5],x[6]))
    area.append(x[5])


    if x[6] != "''" and " (" not in x[6]:
        country.append(x[6])

    elif " (" in y[1]:
        k = y[1].split(" (")
        country.append(f"{k[0]}-{k[1][:-1]} Border")

    elif ")'" in y[1]:
        k = y[1].split(" (")
        country.append(f"{k[0]}-{k[1][:-2]} Border")

    else:
        y = x[5].split(" ")
        if y[-1] == "Region'":
            if "-" in y[1]:
                country.append(f"{y[1]} Border")
            else:
                country.append(y[1])
        else:
            country.append(y[-1])


# print(fn)
# print()
# print(area)
# print()
# print(country)

earthquakeINfo = {"Date": date,"Day": day,"Month":month, "Year" : year, "Time (GMT)": time, "Latitude (N)": lat,"Longitude (E)": lng,"Magnitude": mag, "Location": area, "Country": country}

df=pd.DataFrame.from_dict(earthquakeINfo,orient='index').transpose()
pd.set_option('display.max_rows', None)

df


# In[ ]:




