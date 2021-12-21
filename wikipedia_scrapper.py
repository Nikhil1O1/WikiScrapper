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

#grabbing markers for first tag
substr1S = lst[0]
substr1E = lst[1]

#index for first content
sb1s = string.find(substr1S)
sb1e = string.find(substr1E)

#grabbing  markers for second tag
substr2S = lst[1]
substr2E = lst[2]

#index for second content
sb2s = string.find(substr2S)
sb2e = string.find(substr2E)

#index for third content

substr3S = lst[2]
substr3E = lst[3]

sb3s = string.find(substr3S)
sb3e = string.find(substr3E)

#printing history

his = string[sb1s:sb1e]
his = re.sub(r"(\{(.*?)\})(\s.{0,})", "", his)

#printing captured tag name
helper.tagName(substr1S)

soup_his = BeautifulSoup(his,'lxml')
tmp = soup_his.select('p')
his_content = '\n'.join([ para.text for para in tmp[:]])
print(his_content)

#printing captured tag name
wrtSys = string[sb2s:sb2e]
wrtSys = re.sub(r"(\{(.*?)\})(\s.{0,})", "", wrtSys)

helper.tagName(substr2S)


soup_wrt = BeautifulSoup(wrtSys,'lxml')
tmp = soup_wrt.select('p')
wrt_content = '\n'.join([ para.text for para in tmp[:]])
print(wrt_content)

#printing captured tag name
helper.tagName(substr3S)
otherUses = string[sb3s:sb3e]
otherUses = re.sub(r"(\{(.*?)\})(\s.{0,})", "", otherUses)

soup_oth = BeautifulSoup(otherUses,'lxml')
tmp = soup_oth.select('p')
oth_content = '\n'.join([ para.text for para in tmp[:]])
print(oth_content)