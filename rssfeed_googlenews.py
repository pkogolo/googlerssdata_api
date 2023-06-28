#this python application application retrieves
#top stories from Google News by scrapping news
#data from google rrs feed site

#1. Import the required libraries
#2. Specify the news URL and open the connection
#3. Parse the XML data using BeautifulSoup
#4. Find all the "item" tags, which represent individual news article
#5. Print the news title, URL, and publish date for each news article

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

#establish connection between my terminal and
#the google news RSS feed site
googlenews_url = "https://news.google.com/news/rss"
Client = urlopen(googlenews_url)
xml_content = Client.read()
Client.close()

soup_page = soup(xml_content, "xml")
news_list = soup_page.find_all("item")
#print details 
for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print("_"*60) #prints a visual separator line of underscores (_)60 times