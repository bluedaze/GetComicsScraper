import requests
from bs4 import BeautifulSoup
import time
import urllib.parse
import datetime
import os

downloaded = 1
links = []
advance = []

def file_handling():

    # Keeps a log of all pages which have been saved.
    with open("downloaded_urls.txt", "+a") as file:
            file.write(str(links))

    # Removes link which was fetched and downloaded.
    links.pop(0)

    # Opens file and deletes contents.
    open("comic_urls.txt", "w").close()

    # Rewrites links[] to comic_urls.txt without the poppped element. Basically moves on to the next
    # item in the queue automatically.
    with open ("comic_urls.txt", "w") as f:
        for i in links:
            f.write(i)

def fetch_download():
    def broken():
        time.sleep(2)
        print("***********************".center(100))
        print("Broken Link".center(100), end = "")
        print("*")
        print("Skipping Download".center(100), end = "")
        print("*")
        print("***********************".center(100))
        print("\n\nAdding this link to brokenlinks.txt in your current working directory\n\n")
        print("\n\n")
        print("Next File".center(110, "-"))
        print("\n\n")
        with open("brokenlinks.txt", "a+") as outfile:
            outfile.write(link + "\n")
        time.sleep(3)
    
    for link in advance:
        page = requests.get(link)
        soup = BeautifulSoup(page.text, "html.parser")
        
    attempts = 0
    while attempts < 3:
        attempts += 1
        try:
            comic_title = soup.find("h1", class_="post-title").get_text()
            print("\n\nGoing to download link...\n\n")
            break
        except:
            print("There seems to be an issue rendering this page correctly.",
                  "Attempting to retry. Retry " + str(attempts) + " of 3 times")

    current_title = "Saving the current title: " + str(comic_title) + "\n\n"
    
    print(current_title.center(100))
    

    download_button = soup.find("a", class_="aio-red")




    if download_button is not None:
        link = download_button.get("href")
        s = requests.Session()
        r = s.get(link, allow_redirects=False)
        redirect_url = r.headers['location']
        r = requests.head(redirect_url)
        file_size = r.headers.get('content-length')

        if file_size is not None:
            decoded_url = urllib.parse.unquote(redirect_url)
            print("\nWriting file from: ", decoded_url, "\n")
            filename = decoded_url.rsplit('/', 1)[-1]
            file_path = ("/data2/GetComics.Info_Downloads/")
            file_location = file_path + filename

            
            if os.path.exists(file_location):
                first_byte = os.path.getsize(file_location)
            else:
                first_byte = 0
                
            headers = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
            r = s.get(redirect_url, headers=headers, stream = True, verify=False)
       
            print("File is being saved as: ", '"', filename, '"', sep="")

            with open(file_location, 'ab') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)



            print("\n\n")
            print("_______________________".center(100))
            print("")
            print("File written!".center(100))
            print("_______________________".center(100))
            print("\n\n")
            print("Next File".center(100, "-"))
            print("\n\n")
        else:
            broken()

    else:
        broken()


#####################################################################################################



                                    #      __  ___        _      
                                    #     /  |/  /____ _ (_)____ 
                                    #    / /|_/ // __ `// // __ \
                                    #   / /  / // /_/ // // / / /
                                    #  /_/  /_/ \__,_//_//_/ /_/



                                    
#####################################################################################################


try:
    print("\n\n\n\nAttempting to fetch list from local directory...\n\n")
    with open ("comic_urls.txt", "r") as f:
        for item in f:
            links.append(item)
    time.sleep(1.5)
except FileNotFoundError:
    print("\n\n\n\n\--------------------ERROR--------------------".center(100))
    print("\n\nA list is required to fetch downloads.")
    time.sleep(3)
    print("\nPlease add a list of urls to your current working directory as comic_urls.txt\n\n")
    time.sleep(1.5)
    input("Press Enter to exit program.")

with open("comic_urls.txt") as f:
        for i in range(1000):
            data = f.readline()
            data = data.strip("\n")
            advance.append(data)
            currentDT = datetime.datetime.now()
            time_of_pass = ("Current time is: " + currentDT.strftime("%I:%M:%S %p"))
            pass_count = "Preparing pass: " + str(downloaded) + " of " + str(1000)
            print("\n")
            print(time_of_pass.center(100))
            print("~~~~~~~~~~~~~~~~~".center(100))
            print(pass_count.center(100))
            print("\n")
            time.sleep(2)
            downloaded = downloaded + 1
            fetch_download()
            advance.clear()
            file_handling()
