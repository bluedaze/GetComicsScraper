import requests
from bs4 import BeautifulSoup
import time

page = requests.get('https://getcomics.info/sitemap/')
soup = BeautifulSoup(page.text, 'lxml')

def link_grabber():
    comicbooks = []

    listcontents = soup.find("div", class_="su-spoiler su-spoiler-style-fancy su-spoiler-icon-plus su-spoiler-closed")

    for item in listcontents.find_all('ul'):
        for link in item.find_all('li'):
            for comic in link.find_all('a'):
##                print(comic.get('href'))
                comicbooks.append(comic.get('href'))

    comics = set(comicbooks)

    bad_links = {"https://getcomics.info/sitemap/?lcp_page0=2#lcp_instance_0", "https://getcomics.info/sitemap/?lcp_page0=3#lcp_instance_0", "https://getcomics.info/sitemap/?lcp_page0=4#lcp_instance_0", "https://getcomics.info/sitemap/?lcp_page0=5#lcp_instance_0",
         "https://getcomics.info/sitemap/?lcp_page0=6#lcp_instance_0", "https://getcomics.info/sitemap/?lcp_page0=77#lcp_instance_0", "https://getcomics.info/sitemap/?lcp_page0=2#lcp_instance_0", "https://getcomics.info/sitemap/?lcp_page0=51#lcp_instance_0",
         "https://getcomics.info/sitemap/?lcp_page0=60#lcp_instance_0"}

    comics.difference_update(bad_links)

    outfile = open("comiclinkreport.txt", "a+")
    for item in comics:
        outfile.write(item + "\n")
    time.sleep(1.5)
    print("\nYour links have been collated into a file in your current working directory")
    time.sleep(1.5)

url = ("https://getcomics.info/sitemap/?lcp_page0=")

links = []
count = 0
for item in range(77):
    count = count + 1
    link = url+str(count)
    links.append(link)

for address in links:
    nextpage = requests.get(address)
    soup = BeautifulSoup(page.text, 'lxml')
    print("\nWe have navigated to the next page\n")
    print("\n\tCurrent page: ", address)
    print("\n\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1.5)
    link_grabber()
    print("\nzzZzzZz\n")
    time.sleep(1)
    print("S", end = "")
    time.sleep(1)
    print("l", end = "")
    time.sleep(1)
    print("e", end = "")
    time.sleep(1)
    print("e", end = "")
    time.sleep(1)
    print("p", end = "")
    time.sleep(1)
    print("i", end = "")
    time.sleep(1)
    print("n", end = "")
    time.sleep(1)
    print("g", end = "")
    time.sleep(1)
    print(".", end = "")
    time.sleep(1)
    print(".", end = "")
    time.sleep(1)
    print(".", end = "")
    time.sleep(1)
    print("\n\n")
    time.sleep(2)
