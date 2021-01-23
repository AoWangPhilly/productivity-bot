'''
FILE: scraper.py
AUTHOR: Ao Wang
DESCRIPTION: Scraped website and called GIPHY API to collect Gordon Ramsay quotes, memes, and gifs
DATE: 01/23/2021
'''

from bs4 import BeautifulSoup
import requests
from random import choice
import json
import pickle
from typing import List
from os.path import join
from selenium import webdriver
from time import sleep
import re

# ---------------------------- GLOBAL VARS--------------------------------
MEME_URL = 'https://www.scoopwhoop.com/humour/gordon-ramsay-memes/'
QUOTES_URL = 'https://www.scarymommy.com/gordon-ramsay-memes-quotes/'
DRIVER_PATH = '/Users/aowang/Desktop/chromedriver'
# ------------------------------------------------------------------------

# --------------------------- GIPHY KEY ----------------------------------
with open('giphy_key', 'r') as f:
    KEY = f.read()
# ------------------------------------------------------------------------


def scrape_memes() -> List[str]:
    '''Scapes G.R. memes

    :returns: the scraped G.R. meme URL's 
    :rtype: list of strings
    '''
    # Make requests to page
    meme_page = requests.get(MEME_URL)
    meme_soup = BeautifulSoup(meme_page.content, 'html.parser')

    # Find all memes in https://www.scoopwhoop.com/humour/gordon-ramsay-memes/
    img_tags = meme_soup.findAll('img')
    img_url_lst = []

    # Loop throug image tags and gather the data-src attribute
    for meme in img_tags:
        img_url = meme['data-src']
        # The images are stored in a ramsayy folder
        if 'ramsayy' in img_url:
            img_url_lst.append(img_url)
    return img_url_lst


def scrape_quotes():
    '''Scrapes G.R. quotes using Selenium since the text was dynamic

    :returns: the scraped G.R. quotes
    :rtype: list of strings
    '''

    # Headless chrome driver
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(
        executable_path=DRIVER_PATH, options=options)
    driver.get(QUOTES_URL)

    # Sleep for 1 second to let the page load fully
    sleep(1)

    # Get the HTML code and quit the driver
    quote_soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # Find all the quotes
    quotes = quote_soup.findAll('p')
    quotes_lst = []

    # Clean up the quotes
    for quote in quotes:
        quote = quote.text
        if re.match('\d.*', quote):
            quote = quote[4:-1]
            quote = quote.replace('“', '')
            quotes_lst.append(quote)
    return quotes_lst


def call_giphy_gifs():
    '''Calls the GIPHY API to get G.R. GIFs

    :returns: the scraped G.R. GIFs urls
    :rtype: list of strings
    '''
    LIMIT = 20
    # Use giphy SDK to grab amount of Gordon Ramsay gifs

    # INFO: https://developers.giphy.com/docs/api/endpoint#search
    encoded_gifs = requests.get(
        f'http://api.giphy.com/v1/gifs/search?q=gordon+ramsay&api_key={KEY}&limit={LIMIT}').content
    gifs = json.loads(encoded_gifs.decode('utf8'))
    gifs_lst = [gif['embed_url'] for gif in gifs['data']]
    return gifs_lst


def save_as_pickle(lst: List[str], fname: str) -> None:
    '''Save Python lists as pickle files, therefore it'll be easier
       when Discord bot goes in to read in random meme or quote.

    lst: the list of URL's of images or quotes
    lst: list of strings
    fname: the filename of the pickle file
    fname: str
    '''
    fname = join('..', '..', 'db', 'img', fname+'.pkl')
    with open(fname, 'wb') as f:
        pickle.dump(lst, f)


if __name__ == '__main__':

    # save_as_pickle(scrape_memes(), 'Memes')
    # save_as_pickle(call_giphy_gifs(), 'GIFs')
    # save_as_pickle(scrape_quotes(), 'Quotes')
    base_img_path = join('..', '..', 'db', 'img')
    meme = join(base_img_path, 'Memes.pkl')
    gif = join(base_img_path, 'GIFs.pkl')
    quote = join(base_img_path, 'Quotes.pkl')

    with open(meme, 'rb') as f:
        meme_lst = pickle.load(f)

    with open(gif, 'rb') as f:
        gif_lst = pickle.load(f)

    with open(quote, 'rb') as f:
        quote_lst = pickle.load(f)

    print(meme_lst)
    print(gif_lst)
    print(quote_lst)
