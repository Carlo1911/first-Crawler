from bs4 import BeautifulSoup
from threading import Thread
import urllib.request

#Ubicación de restaurantes
home_url = "https://www.yelp.com"
find_what = "Restaurants"
location = "London"
page = "&start=" # 0 10 20
#Obtener todos los restaurantes con el criterio de búsqueda
url = []
for i in range(10):
    search_url = home_url + "/search?find_desc=" + find_what + "&find_loc" + location + page + str(i*10)
    s_html = urllib.request.urlopen(search_url).read()
    soup_s = BeautifulSoup(s_html, "lxml")

    #Obtener los 10 primeros
    s_urls = soup_s.select('.biz-name')[:10]
    for u in range(len(s_urls)):
        print(home_url + s_urls[u]['href'])
        url.append(home_url + s_urls[u]['href'])

def scrape(ur):
    html = urllib.request.urlopen(ur).read()
    soup = BeautifulSoup(html,"lxml")
    title = soup.select('.biz-page-title')
    saddress = soup.select('.street-address')
    phone = soup.select('.biz-phone')
    if title:
        print ("Title: " + title[0].getText().strip())
    if saddress:
        print ("Street Address: " + saddress[0].getText().strip())
    if phone:
        print ("Phone Number: " + phone[0].getText().strip())
    print ("-------------------")

threadlist = []
i=0
#Making threads to perform scraping
while i<len(url):
    t = Thread(target=scrape,args=(url[i],))
    t.start()
    threadlist.append(t)
    i=i+1
for t in threadlist:
    t.join()