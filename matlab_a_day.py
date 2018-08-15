###############-----Matlab-A-Day Process Flow-----####################

###Step One: Matlab Runs Python script for Beautiful Soup (henceforth BS)

###Step Two: BS scrape links  tool box ex categories 
#from navbar on 'https://www.mathworks.com/examples' then scraped all sub-categores from 
#'https://www.mathworks.com/examples/product-group/.....' & puts them in array of arrys

###Step 3: Send hierarchical categories array back to user to choose from  (GUI un-check list)

###Step 4: Given user choices run another BS script to scrape selected ex pages

from bs4 import BeautifulSoup
from csv import writer
import requests

###example_scraper is a fct which consumes a URL with which to scrape all link from
def example_scraper (page_link = 'https://www.mathworks.com/examples/computer-vision'):
    
    # fetch the content from url
    page_response = requests.get(page_link, timeout=5)
    # parse html
    page_content = BeautifulSoup(page_response.content, "html.parser")
    
    # extract all html elements where price is stored
    link_tags = page_content.find_all(class_='card_container')
    
    urlArray = []
    titleArray = []

    with open('links.csv','w',newline='') as csv_file:
        csv_writer = writer(csv_file)
        headers = ['Title', 'URL']
        csv_writer.writerow(headers)
    
        for tag in link_tags:
            title = tag.find(class_='panel-heading').get_text().replace('\n','')
            url = "https://www.mathworks.com" + tag.find('a')['href']
            titleArray.append(title)
            urlArray.append(url)
            csv_writer.writerow([title, url])
            
    pageDict = {"titles":titleArray, "urls": urlArray}
    
    return pageDict

dictionaryTest = example_scraper()
    
###end example_scraper