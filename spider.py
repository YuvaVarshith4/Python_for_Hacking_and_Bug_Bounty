# PRACTICE: WEB SCRAPING WITH BEAUTIFUL SOUP

# https://en.wikipedia.org/wiki/Programmer#

# import requests
# from bs4 import BeautifulSoup

# def get_page(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     print(soup.title.string)
#     # print(soup.find('h1'))
#     # print(soup.find_all('p')[10])
#     # print(soup.find('a'))
#     # var = soup.find(id = "mw-searchButton")
#     # print(var.text)
#     tag = soup.find_all("a")
#     for t in tag:
#         print(t.get("href"))

# get_page(input("What URL would you like to scrape? "))


# TOOL BUILDING

# https://www.python.org
import requests
from bs4 import BeautifulSoup

from urllib import *
from urllib.parse import urljoin

visited_urls = set()

def spider_urls(url, key_word):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed for : {url}")
        return    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get ("href")
            if href is not None and href !="" :
                urls.append(href)
        # print(urls)
        for url1 in urls:
            if url1 not in visited_urls:
                visited_urls.add(url1)
                url_join = urljoin(url, url1)
                if key_word.lower() in url_join.lower():
                    print(f"Found '{key_word}' in URL: {url_join}")
                    spider_urls(url_join, key_word)
                else: 
                    pass    


url = input("enter the url you want to scrape: ")
key_word= input("Enter the keyword to search for int the URL provided. ")
spider_urls(url, key_word)
