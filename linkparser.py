# TO DO:
# Write a function which checks for file on 32pag.es

import requests
from bs4 import BeautifulSoup
import time
import urllib.parse

links = []
advance = []

def main():
    count = 1
    userchoice = int(input("How many links would you like to download? Please enter a number: "))
    print("\n\n")
    with open("comic_urls.txt") as f:
            for i in range(userchoice):
                data = f.readline()
                data = data.strip("\n")
                advance.append(data)
                print("\t\t\t Preparing pass", count, "of", userchoice)
                count = count + 1
                fetch_download()
                advance.clear()
                downloaded()
                delete_downloaded_item()



def load_list():
    with open ("comic_urls.txt", "r") as f:
        for item in f:
            links.append(item)

def delete_downloaded_item():

    links.pop(0)

    #opens file and deletes contents
    open("comic_urls.txt", "w").close()

    with open ("comic_urls.txt", "w") as f:
        for i in links:
            f.write(i)

def downloaded():
    with open("downloaded_urls.txt", "+a") as file:
            file.write(str(links))

def fetch_download():
    for link in advance:
        page = requests.get(link)
        soup = BeautifulSoup(page.text, "html.parser")
        
    comic_title = soup.find("h1", class_="post-title").get_text()
    print("\n\nGoing to download link...\n\n")

    print("\tSaving the current title:", comic_title, "\n\n")

    download_button = soup.find("a", class_="aio-red")
    try:
        link = download_button.get("href")

        r = requests.get(link, allow_redirects=False)

        redirect_url = r.headers['location']

        decoded_url = urllib.parse.unquote(redirect_url)
        
        r = requests.get(redirect_url, stream = True, timeout=(10, 27))

        filename = decoded_url.rsplit('/', 1)[-1]

        file_path = ("/data2/GetComics.Info_Downloads/")

        file_location = file_path + filename

        print("\nWriting file from: ", decoded_url, "\n")

        print("File is being saved as: ", '"', filename, '"', sep="")

        open(file_location, 'wb').write(r.content)

        print("\n")
        print('''
        \t\t_______________________

        \t\t    File written!
        \t\t_______________________\n\n''')
    except AttributeError:
        print("The link for this comic is currently broken\n")
        time.sleep(2)
        print('''
        \t\t***********************

        \t\t    Broken Link
        \t\t\tSkipping Download
        \t\t***********************\n\n''')
        print("Adding this link to brokenlinks.txt in your current working directory\n\n")
        print("----------------\n\n")
        outfile = open("brokenlinks.txt", "a+")
        outfile.write(link + "\n\n")
        outfile.close()
        time.sleep(3)

try:
    print("\n\n\n\nAttempting to fetch list from local directory...\n\n")
    load_list()
    time.sleep(1.5)
    main()
    downloaded()
except FileNotFoundError:
    print("\n\n\n\n\t--------------------ERROR--------------------")
    print("\n\nA list is required to fetch downloads.")
    time.sleep(3)
    print("\nPlease add a list of urls to your current working directory as comic_urls.txt\n\n")
    time.sleep(1.5)
    input("Press Enter to exit program.")
