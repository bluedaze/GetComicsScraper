import requests
from bs4 import BeautifulSoup

outfile = open("comiclist.txt", "w")
page = requests.get('https://getcomics.info/sitemap/')
soup = BeautifulSoup(page.text, 'lxml')
body = soup.findAll("a")
outfile.write = (body)
