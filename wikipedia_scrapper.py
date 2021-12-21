#managing imports
from bs4 import BeautifulSoup
import re
import requests
import helper


#input your name

inp = helper.ask_name()
page = requests.get("https://en.wikipedia.org/wiki/"+inp[0])

soup = BeautifulSoup(page.content,"lxml")

#converting html to string for parsing
string = str(soup)
lst = helper.tagSearch(string)

tot_no_of_time_toPrint = 3 #bydefault and should not be more than total number 
                             #of subheading in the page

for i in range(tot_no_of_time_toPrint):
    substrS = lst[i]
    substrE = lst[i+1]

    sb1s = string.find(substrS)
    sb1e = string.find(substrE)
    contentString = string[sb1s:sb1e]
    contentString = re.sub(r"(\{(.*?)\})(\s.{0,})", "", contentString)  #using regular expression to filter anomalies

    #printing captured tag name
    helper.tagName(substrS)

    soup = BeautifulSoup(contentString,'lxml')
    tmp = soup.select('p')
    contentFinale = '\n'.join([ para.text for para in tmp[:]])
    print(contentFinale)
    helper.saveOutput(contentFinale)