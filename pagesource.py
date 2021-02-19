from bs4 import BeautifulSoup
from random import randrange
import requests
from requests.api import get

# input:  a string that has potentially bad characters
# return: a cleaned (safe) string
def inputCleanser(dirtyString):
    cleanString = ''
    for c in dirtyString.strip():
        if c.isalnum or c.isspace:
            cleanString += c
        elif c == '?':
            cleanString += c
        else:
            cleanString += ' '
    return cleanString

USER_AGENTS = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    )

def getHtml(url):
    userAgent = USER_AGENTS[randrange(len(USER_AGENTS))]
    headers = {'user-agent': userAgent}
    htmlContent = requests.get(url, headers=headers).text
    soup = BeautifulSoup(htmlContent, 'lxml')
    return soup


if __name__ == "__main__":
    print('Hello')
    url = input('Paste site URL: ')
    htmlSource = getHtml(url)

    option = inputCleanser(input('Do you want to print (p) or save (s) the page source?: ')).lower()
    while option not in ['p', 's']:
        option = inputCleanser(input("Sorry, didn't get that. Try again: ")).lower()
    if option == 'p':
        print(htmlSource)
    elif option == 's':
        print('Saving HTML.')

