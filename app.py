#this python application application retrieves
#top stories from Google News by scrapping news
#data from google rrs feed site

#1. Import the required libraries
#2. Specify the news URL and open the connection
#3. Parse the XML data using BeautifulSoup
#4. Find all the "item" tags, which represent individual news article
#5. Print the news title, URL, and publish date for each news article

from flask import Flask
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import json


app = Flask(__name__)
@app.route('/')
#establish connection between my terminal and
#the google news RSS feed site
def googlenews():
    googlenews_url = "https://news.google.com/news/rss"
    Client = urlopen(googlenews_url)
    xml_content = Client.read()
    Client.close()

    soup_page = soup(xml_content, "xml")
    news_list = soup_page.find_all("item")
    #print details 
    #for news in news_list:
        #print(news.title.text)
        #print(news.link.text)
        #print(news.pubDate.text)
        #print("_"*60) #prints a visual separator line of underscores (_)60 times
        
    # but to send the datat to server instead of printing
    # capture the data in an empty array and send as a JSON
    grssfeed = []
    for news in news_list:
        news_data = {
            "title": news.title.text,
            "link": news.link.text,
            "pubDate": news.pubDate.text
        }
        grssfeed.append(news_data)
    # Convert the data_to_send list to a JSON string
    return json.dumps(grssfeed)

if __name__ == "__main__":
	#app.run()
    app.run(host='0.0.0.0', port=5000)