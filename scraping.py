import requests
import fontstyle
import bs4

headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
          }

print()

topic = fontstyle.apply('Scraping Google Results in PYTHON','bold/BLACK/CYAN_BG')
print(topic)

print()

print()
query = input("Enter your Query : ")
print()

g = ('\033[3m'+"Searching....."+'\033[0m')
print('\033[1m'+(g)+'\033[0m')

print()

print('-'*100)

print()
url = "https://www.google.com/search?q="+query

google_search = requests.get(url,headers=headers)

soup = bs4.BeautifulSoup( google_search.text , "html.parser" )

heading_object=soup.find_all('h3')
link = soup.find_all("div",{"class":"yuRUbf"})

for i,j in zip(link,heading_object):
  print()
  print('\033[1m' + i.getText(" \n ") +'\033[0m')
  print()
  print("-"*100)
