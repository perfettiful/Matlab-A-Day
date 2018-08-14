from bs4 import BeautifulSoup
from csv import writer
import requests

page_link = 'https://www.mathworks.com/examples/signal/category/signal-generation-and-preprocessing'
page_response = requests.get(page_link, timeout = 5)

page_content = BeautifulSoup(page_response.content, "html.parser")

link_tags = page_content.find_all(class_='card_container')

with open('links.csv','w',newline='') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'URL']
    csv_writer.writerow(headers)

    for tag in link_tags:
        title = tag.find(class_='panel-heading').get_text().replace('\n','')
        url = "https://www.mathworks.com" + tag.find('a')['href']
        csv_writer.writerow([title, url])

print(title)
print(url)