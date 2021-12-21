import re
import string
import codecs

def tagSearch(soup):
    reg_str = "<" + 'h2' + ">(.*?)</" + 'h2' + ">"
    res = re.findall(reg_str,soup)
    for i in range(len(res)):
        res[i] = '<h2>'+res[i]+'</h2>'

    return(res)


def tagName(s):
    start = s.find('">') + len('">')
    end = s.find('</')
    substring = s[start:end]
    print(substring)
    saveOutput(substring)
    print("")
    saveOutput('\n')


def ask_name():
    while True:
        name = input("What is your name? ")
        if name.isalpha():
            return name
        else:
            print("Please use only letters, try again")

def saveOutput(s):
    file = codecs.open("Output.txt", "a", "utf-8")
    file.write(s)
    file.close()