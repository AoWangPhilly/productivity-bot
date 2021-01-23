'''


'''

from bs4 import BeautifulSoup
import requests
from random import choice
import json
import pickle
from typing import List
from os.path import join

# ---------------------------- URLS --------------------------------
MEME_URL = 'https://www.scoopwhoop.com/humour/gordon-ramsay-memes/'
QUOTES_URL = 'https://www.scarymommy.com/gordon-ramsay-memes-quotes/'
# ------------------------------------------------------------------

# --------------------------- GIPHY KEY ----------------------------
with open('giphy_key', 'r') as f:
    KEY = f.read()
# ------------------------------------------------------------------


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
    # Make requests to pages
    meme_page = requests.get(MEME_URL)
    quotes_page = requests.get(QUOTES_URL)

    # Make them into Beautiful Soup objects
    meme_soup = BeautifulSoup(meme_page.content, 'html.parser')
    quotes_soup = BeautifulSoup(quotes_page.content, 'html.parser')

    # Find all memes in https://www.scoopwhoop.com/humour/gordon-ramsay-memes/
    img_tags = meme_soup.findAll('img')
    img_url_lst = []

    for meme in img_tags:
        img_url = meme['data-src']
        if 'ramsayy' in img_url:
            img_url_lst.append(img_url)

    LIMIT = 20
    # Use giphy SDK to grab amount of Gordon Ramsay gifs

    # INFO: https://developers.giphy.com/docs/api/endpoint#search
    encoded_gifs = requests.get(
        f'http://api.giphy.com/v1/gifs/search?q=gordon+ramsay&api_key={KEY}&limit={LIMIT}').content
    gifs = json.loads(encoded_gifs.decode('utf8'))
    gifs_lst = [gif['embed_url']for gif in gifs['data']]

    save_as_pickle(img_url_lst, 'Memes')
    save_as_pickle(gifs_lst, 'GIFs')
