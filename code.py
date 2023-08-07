# for cast [ we will have 2nd call]
import requests
import re
from bs4 import BeautifulSoup
from googlesearch import search

#year of release  --> done
#duration of movie  -->done  done
#starring   -->done done
#director  --> done done
#genres   --> done by just watch
#short summary --> done by justwatch

query = "Waltair Veerayya /justwatch "
url = ""

my_results_list = []

for i in search(query,        # The query you want to run
                tld = 'com',  # The top level domain
                lang = 'en',  # The language
                num = 10,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = None,  # Last result to retrieve
                pause = 2.0,  # Lapse between HTTP requests
               ):
    #my_results_list.append(i)
    if("https://www.justwatch.com/" in i):
      url  = i
      break

response = requests.get(url)

arr_cast = []

if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, "lxml")
    # Example: Extract all the links on the page

    div_class = 'hidden-horizontal-scrollbar__items'
    div_ = soup.find('div', class_=div_class)
    for i in div_:
      x = i.find_all('a', class_='title-credit-name')
      y = i.find_all('div',class_='title-credits__actor--role--name')
      for j , k in zip(x,y) :
        arr = []
        arr.append(j.get_text())
        arr.append(k.get_text())
        arr_cast.append(arr)
    print(arr_cast)  

