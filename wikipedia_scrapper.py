from bs4 import BeautifulSoup
import urllib
import requests


page = requests.get("https://en.wikipedia.org/wiki/N")

soup = BeautifulSoup(page.content,"lxml")

#converting html to string for parsing
string = str(soup)

#grabbing history
substr1S = '<h2><span class="mw-headline" id="History">History</span></h2>'
substr1E = '<h2><span class="mw-headline" id="Use_in_writing_systems">Use in writing systems</span></h2>'

#index for first content
sb1s = string.find(substr1S)
sb1e = string.find(substr1E)

#grabbing use in writing systems
substr2S = '<h2><span class="mw-headline" id="Use_in_writing_systems">Use in writing systems</span></h2>'

substr2E = '<h2><span class="mw-headline" id="Other_uses">Other uses</span></h2>'


#index for second content
sb2s = string.find(substr2S)
sb2e = string.find(substr2E)


#index for third content

substr3S = '<h2><span class="mw-headline" id="Other_uses">Other uses</span></h2>'
substr3E = '<h2><span class="mw-headline" id="Related_characters">Related characters</span></h2>'


#printing history

his = string[sb1s:sb1e]


print("History")
print("")

soup_his = BeautifulSoup(his,'lxml')
tmp = soup_his.select('p')
his_content = '\n'.join([ para.text for para in tmp[:]])
print(his_content)

#printing writing systems

wrtSys = string[sb2s:sb2e]

print("Use in writing systems")
print("")


soup_wrt = BeautifulSoup(wrtSys,'lxml')
tmp = soup_wrt.select('p')
wrt_content = '\n'.join([ para.text for para in tmp[:]])
print(wrt_content)