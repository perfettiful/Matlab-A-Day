#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 17:40:22 2018

@author: nathanperfetti
"""

###############-----Matlab-A-Day Process Flow-----####################

###Step One: Matlab Runs Python script for Beautiful Soup (henceforth BS)

###Step Two: BS scrape links  tool box ex categories 
#from navbar on 'https://www.mathworks.com/examples' then scraped all sub-categores from 
#'https://www.mathworks.com/examples/product-group/.....' & puts them in array of arrys

###Step 3: Send hierarchical categories array back to user to choose from  (GUI un-check list)

###Step 4: Given user choices run another BS script to scrape selected ex pages




###############------------------------------------####################

from bs4 import BeautifulSoup
import requests

###example_scraper is a fct which consumes a URL with which to scrape all link from
def example_scraper (page_link = 'https://www.mathworks.com/examples/computer-vision'):
    
    # fetch the content from url
    page_response = requests.get(page_link, timeout=5)
    # parse html
    page_content = BeautifulSoup(page_response.content, "html.parser")
    
    # extract all html elements where price is stored
    link_tags = page_content.find_all(class_='card_container')
    
    print(link_tags[0])
    # Returns following card tag:
    # <div class="card_container explorer_view add_long_title" data-ui-component="card" data-view-count="0" id="example-24078">
    #<a href="/examples/computer-vision/mw/vision-ex30397662-use-local-features">
    #<div class="card_media" style="background-image: url(/examples/thumbnail/24078);">
    #<img alt="24078" src="/examples/thumbnail/24078">
    #</img></div>
    #<div class="card_body">
    #<div class="panel panel_color_transparent panel_color_fill">
    #<div class="panel-heading">
    #<h3>Use Local Features</h3>
    #</div>
    #<div class="panel-body">
    #<p class="card_description">Registering two images is a simple way to understand local features. This example finds a geometric transformation between two images. It uses local features to find well-localized anchor</p>
    #</div>
    #</div>
    #</div>
    #</a> <div class="card_footer">
    #<div class="card_source">
    #<!-- Source: MW -->
    #<div class="card_type" data-placement="top" data-toggle="tooltip" title="MathWorks">
    #<span aria-hidden="true" class="icon-membrane"></span>
    #</div>
    #</div>
    #</div>
    #</div>
    
    # you can also access the main_price class by specifying the tag of the class
    #prices = page_content.find_all('div', attrs={'class':'card_container'})
    
###end example_scraper